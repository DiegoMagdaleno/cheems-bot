from cheemsbot.helpers import embeds
import discord
from discord.ext import commands
import requests
import datetime
from cheemsbot.helpers.wikipedia import NoArticlesOrNotFound, Wikipedia

bot = commands.Bot(command_prefix=">")


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
        self.embed_message = embeds.WikipediaEmbed(discord.Color.blue(), self.our_wikipedia_message).get_embed_message()

        await ctx.send(embed=self.embed_message)

def setup(bot):
    bot.add_cog(SearchUtilitiesCog(bot))
