from cheemsbot.helpers import embeds
from cheemsbot.helpers import fourchan

import discord
from discord.ext import commands


class FourChanCommandsCog(commands.Cog, name="4chan"):
    """For now it is only a command, with more to come! Allows you to get technology from the /g/ board"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="tech")
    async def tech(self, ctx):
        """Description:  Grans a random post from 4chan's /g/ board and posts it on the chat\nArguments: `None`"""
        target_board = "g"
        fourchan_post = fourchan.FourChanImage(target_board)
        embed_message = embeds.FourChanEmbed(
            discord.Color.green(),
            fourchan_post.topic,
            fourchan_post.image_url,
            target_board,
            fourchan_post.url,
        ).get_embed_message()
        await ctx.send(embed=embed_message)


def setup(bot):
    bot.add_cog(FourChanCommandsCog(bot))
