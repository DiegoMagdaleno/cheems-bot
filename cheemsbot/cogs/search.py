from requests.api import request
from cheemsbot.helpers.ghelper import NoResults
from cheemsbot.helpers import embeds
import discord
from discord.ext import commands
from cheemsbot.helpers.wikipedia import NoArticlesOrNotFound, Wikipedia
import cheemsbot.config as conf
from cheemsbot.helpers.paginator import ImagePaginator, UrbanPagintor
from cheemsbot.helpers.github import GitHub, GitHubRepositoryError
from cheemsbot.helpers.urban_dictionary import UrbanDictionary, UrbanDictionaryError
from cheemsbot.helpers import errorhandler
from cheemsbot.helpers import brew


class SearchUtilitiesCog(commands.Cog, name="Search"):
    """A collection of commands to help you search without leaving Discord"""

    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(name="wikipedia")
    async def wikipedia(self, ctx, *, query=None):
        """Description:  Displays information about a Wikipedia article in channel.\nArguments: `1`"""
        self.query = query
        if self.query is None:
            await ctx.send(
                embed=errorhandler.BotAlert("warn", "You need to give me a query!"
                ).get_error_embed()
            )
            return
        try:
            self.our_wikipedia_message = Wikipedia(self.query).get_wikipedia_article()
        except NoArticlesOrNotFound:
            await ctx.send(
                embed=errorhandler.BotAlert("error", f"I couldn't find anything for {self.query}"
                ).get_error_embed()
            )
            return
        self.embed_message = embeds.WikipediaEmbed(
            discord.Color.blue(), self.our_wikipedia_message
        )

        await ctx.send(embed=self.embed_message.get_embed_message())

    @commands.command(name="image")
    async def image(self, ctx: commands.Context, *, query=None):
        self.query = query
        self.our_embed_session = discord.Embed()
        self.our_embed_session.title = f"**Search results for {self.query}**"
        self.our_embed_session.description = (
            f"Requested by:  {ctx.message.author.display_name}"
        )
        if self.query is None:
            await ctx.send(
                embed=errorhandler.BotAlert("warn", "You need to give me a query!"
                ).get_error_embed()
            )
            return
        try:
            if ctx.channel.is_nsfw() is False:
                self.array_of_images = conf.get_images(self.query, "high")
            else:
                self.array_of_images = conf.get_images(self.query, "off")
        except NoResults:
            await ctx.send(
                embed=errorhandler.BotAlert("error", f"I couldn't find anything for {self.query}"
                ).get_error_embed()
            )
            return
        await ImagePaginator.paginate(
            pages=self.array_of_images,
            ctx=ctx,
            embed=self.our_embed_session,
            bot=self.bot,
        )

    @commands.command(name="github")
    async def github(self, ctx: commands.Context, *, repository=None):
        self.repository = repository
        if self.repository is None:
            await ctx.send(
                embed=errorhandler.BotAlert("warn", "You need to give me a repository!"
                ).get_error_embed()
            )
            return
        try:
            self.github_session = GitHub(self.repository)
        except GitHubRepositoryError:
            await ctx.send(
                embed=errorhandler.BotAlert("error",
                    f"Had an error getting that repository. Are you sure {self.repository} exists?",
                ).get_error_embed()
            )
            return
        async with ctx.typing():
            self.our_github_respostory = self.github_session.get_github_repo()
            self.our_embed = embeds.GitHubEmbed(
                discord.Color.greyple(), self.our_github_respostory
            )
        await ctx.send(embed=self.our_embed.get_embed_message())

    @commands.command(name="urban")
    async def urban(self, ctx, *, term=None):
        self.term = term
        self.our_embed_session = discord.Embed(color=0x3E9CBF)
        if self.term is None:
            await ctx.send(
                embed=errorhandler.BotAlert("warn", "You need to provide a term!"
                ).get_error_embed()
            )
            return
        try:
            self.definitions = UrbanDictionary(self.term).get_urban_definitions()
        except UrbanDictionaryError:
            self.pure_term = discord.utils.escape_mentions(self.term)
            await ctx.send(
                embed=errorhandler.BotAlert("error", f"Couldn't find anything for that query {self.pure_term}"
                ).get_error_embed()
            )
            return
        await UrbanPagintor.paginate(
            definitions=self.definitions,
            ctx=ctx,
            embed=self.our_embed_session,
            bot=self.bot,
        )

    @commands.command(name="brew")
    async def brew(self, ctx: commands.Context, *, formuale=None):
        if formuale is None:
            await ctx.send(
                embed=errorhandler.BotAlert("error", "You need to give me a formulae."
                ).get_error_embed()
            )
            return
        try:
            self.formuale_session = brew.HomebrewInteracter(
                formuale
            ).get_target_formula()
        except brew.NoHomebrewFormuale:
            await ctx.send(
                embed=errorhandler.BotAlert("error", f"Couldn't find anything for that query {formuale}"
                ).get_error_embed()
            )
            return
        await ctx.send(
            embed=embeds.HomebrewEmbed(self.formuale_session).get_embed_message()
        )

    @commands.command(name="jb")
    async def jb(self, ctx: commands.Context, *, package=None):
        if package is None:
            await ctx.send(
                embed=errorhandler.BotAlert("error", "You need to give me a package to search!"
                ).get_error_embed()
            )
            return
        self.package_response = await JailbreakPackageInteractor(package).get_packages()
        for p in self.package_response:
            await ctx.send("Here you go faggot: " + str(p))


def setup(bot):
    bot.add_cog(SearchUtilitiesCog(bot))
