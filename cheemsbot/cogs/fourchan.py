from discord.ext import commands
from discord.ext.commands.core import command
from cheemsbot.helpers import fourchan, embeds
import discord


class FourChanCommandsCog(commands.Cog, name="4chan commands"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="tech")
    async def tech(self, ctx):
        target_board = "g"
        fourchan_post = fourchan.FourChanImage(target_board)
        embed_message = embeds.FourChanEmbed(
            discord.Color.green(),
            fourchan_post.topic,
            fourchan_post.image_url,
            target_board,
            fourchan_post.url,
        ).getEmbedMessage()
        await ctx.send(embed=embed_message)


def setup(bot):
    bot.add_cog(FourChanCommandsCog(bot))
