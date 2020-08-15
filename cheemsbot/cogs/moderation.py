from cheemsbot.helpers import determiner
from discord.ext import commands
import discord


class StopCommandExecution(Exception):
    pass


class CheemsModerationCog(commands.Cog, name="Moderation"):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(name="kick")
    async def kick(self, ctx, target: discord.User, *, reason=None):
        self.target = target
        has_proper_perms = await determiner.require_proper_permissions(
            ctx, self.target, self.bot
        )

        if not has_proper_perms:
            await ctx.send("Cam't kicmk this user, becaumse it is abomve me.")
            raise StopCommandExecution

        try:
            await ctx.guild.kick(self.target)
            await ctx.send(
                "**{}** has been kicked, \n**Reason:** {}".format(target, reason)
            )
        except discord.ext.commands.errors.CommandInvokeError:
            await ctx.send("Somethimg happemned.")

    @commands.command(name="ban")
    async def ban(self, ctx, target: discord.User, *, reason=None):
        self.target = target
        has_proper_perms = await determiner.require_proper_permissions(
            ctx, self.target, self.bot
        )

        if not has_proper_perms:
            await ctx.send("Cam't bam this user, becumse it is abomve me.")

        try:
            await ctx.guild.ban(self.target)
            await ctx.send(
                "**{}** has been bamned, \n**Reason:** {}".format(target, reason)
            )
        except discord.ext.commands.errors.CommandInvokeError:
            await ctx.send("Somethimg happemned.")


def setup(bot):
    bot.add_cog(CheemsModerationCog(bot))
