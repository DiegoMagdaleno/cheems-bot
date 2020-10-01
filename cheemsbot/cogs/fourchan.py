from cheemsbot.helpers import embeds
from cheemsbot.helpers import fourchan
from cheemsbot import config

from discord.ext import commands


class FourChanCommandsCog(commands.Cog, name="4chan"):
    """A set of commands to get 4chan content without leaving Discord"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="tech")
    async def tech(self, ctx):
        """Description:  Grabs a random post from 4chan's /g/ board and posts it on the chat\nArguments: `None`"""
        self.target_board = "g"
        self.post = config.get_fourchan_post(self.target_board)
        self.embed_message = embeds.FourChanEmbed(
            self.post
        ).get_embed_message()
        await ctx.send(embed=self.embed_message)

    @commands.command(name="4chan")
    async def fourchanpost(self, ctx, *, target_board=None):
        """Description:  Grabs a random post from a user provided board and posts it on the chat, prevents NSFW\nArguments: `None`"""
        self.target_board = target_board
        if self.target_board is None:
            await ctx.send("You need to provide a board.")
            return
        self.four_chan_post = fourchan.FourChanImage(self.target_board)
        if (self.four_chan_post.is_nsfw is False) and (ctx.channel.is_nsfw() is False):
            await ctx.send("Can't display NSFW content in non-NSFW channels.")
            return
        self.embed_message = embeds.FourChanEmbed(
            self.four_chan_post.topic,
            self.four_chan_post.image_url,
            self.target_board,
            self.four_chan_post.url,
        ).get_embed_message()
        await ctx.send(embed=self.embed_message)


def setup(bot):
    bot.add_cog(FourChanCommandsCog(bot))
