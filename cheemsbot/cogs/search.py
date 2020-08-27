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
import pprint


class SearchUtilitiesCog(commands.Cog, name="Search"):
    """A collection of commands to help you search without leaving Discord"""

    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(name="wikipedia")
    async def wikipedia(self, ctx, *, query):
        """Description:  Displays information about a Wikipedia article in channel.\nArguments: `1`"""
        self.query = query
        if self.query is None:
            await ctx.send("You need to give me a query.")
            return
        try:
            self.our_wikipedia_message = Wikipedia(self.query).get_wikipedia_article()
        except NoArticlesOrNotFound:
            await ctx.send(f"Couldn't find an article for {self.query}")
            return
        self.embed_message = embeds.WikipediaEmbed(
            discord.Color.blue(), self.our_wikipedia_message
        ).get_embed_message()

        await ctx.send(embed=self.embed_message)

    @commands.command(name="image")
    async def image(self, ctx: commands.Context, *, query=None):
        self.query = query
        self.our_embed_session = discord.Embed()
        self.our_embed_session.title = "**Search results for {}**".format(self.query)
        self.our_embed_session.description = "Requested by:  {}".format(
            ctx.message.author.display_name
        )
        if self.query is None:
            await ctx.send("You need to give me a query.")
            return
        try:
            if ctx.channel.is_nsfw() is False:
                self.array_of_images = conf.get_images(self.query, "high")
            else:
                self.array_of_images = conf.get_images(self.query, "off")
        except NoResults:
            await ctx.send(f"Couldn't find anything for that query {self.query}")
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
            await ctx.send("You need do give me a repository")
            return
        try:
            self.github_session = GitHub(self.repository)
        except GitHubRepositoryError:
            await ctx.send(
                f"Had an error getting that repository. Are you sure {self.repository} exists?"
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
        self.our_embed_session = discord.Embed(color=0x3e9cbf)
        if self.term is None:
            await ctx.send("Please provide a search term")
            return
        try:
            self.definitions = UrbanDictionary(self.term).get_urban_definitions()
        except UrbanDictionaryError:
            self.pure_term = discord.utils.escape_mentions(self.term)
            await ctx.send(f"Couldn't find anything for your query {self.pure_term}")
            return
        await UrbanPagintor.paginate(
            definitions=self.definitions,
            ctx=ctx,
            embed=self.our_embed_session,
            bot=self.bot,
        )


def setup(bot):
    bot.add_cog(SearchUtilitiesCog(bot))
