from cheemsbot.helpers import embeds
import discord
from discord.ext import commands
from cheemsbot.helpers.wikipedia import NoArticlesOrNotFound, Wikipedia
import cheemsbot.config as conf
from cheemsbot.helpers.paginator import ImagePaginator


def create_tuples(name, urls):
    our_thingy = []
    for i in range(len(urls)):
        our_thingy.append((name, urls[i]))
    return our_thingy


class SearchUtilitiesCog(commands.Cog, name="Search"):
    """A collection of commands to help you search without leaving Discord"""

    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(name="wikipedia")
    async def wikipedia(self, ctx, *, query):
        """Description:  Displays information about a Wikipedia article in channel.\nArguments: `1`"""
        self.query = query
        if self.query is None:
            await ctx.send("Youm neemd to give something to search.")
            return
        try:
            self.our_wikipedia_message = Wikipedia(self.query).get_wikipedia_article()
        except NoArticlesOrNotFound:
            await ctx.send("Ummm I coumlndt fimd anymthing.")
            return
        self.embed_message = embeds.WikipediaEmbed(
            discord.Color.blue(), self.our_wikipedia_message
        ).get_embed_message()

        await ctx.send(embed=self.embed_message)

    @commands.command(name="image")
    async def image(self, ctx: commands.Context, *, query=None):
        self.query = query
        self.our_embed_session = discord.Embed()
        self.our_embed_session.title = '**Search results for {}**'.format(self.query)
        self.our_embed_session.description = 'Requested by:  {}'.format(ctx.message.author.display_name)
        if self.query is None:
            await ctx.send("Ummmm, an imamge for whamt")
            return
        self.array_of_images = conf.get_images(self.query, "off")
        self.thing = create_tuples(self.query, self.array_of_images)
        await ImagePaginator.paginate(
            pages=self.array_of_images, ctx=ctx, embed=self.our_embed_session, bot=self.bot
        )


def setup(bot):
    bot.add_cog(SearchUtilitiesCog(bot))
