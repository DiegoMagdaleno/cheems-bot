from cheemsbot.helpers import random_operations

import discord
from discord.ext import commands


class CheemsRootCommandsCog(commands.Cog, name="Root"):
    """Root is a set of actions for general debugging of the bot"""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="ping")
    async def ping(self, ctx):
        """Tells you the client latency between the bot and the Discord client"""
        self.random_cheems = random_operations.get_cheems_phrase()
        self.ping_in_ms = round(self.bot.latency * 1000, 1)
        await ctx.send(
            self.random_cheems + " \n**{:.0f}{}".format(self.ping_in_ms, "ms** pimg")
        )


def setup(bot):
    bot.add_cog(CheemsRootCommandsCog(bot))
