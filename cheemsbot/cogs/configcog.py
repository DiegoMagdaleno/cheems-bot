from discord.ext import commands

class Config(commands.Cog, name="Configuration"):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="prefix")
    async def prefix(self, ctx, *, prefix=">"):
        await self.bot.config.upsert({"_id": ctx.guild.id, "prefix": prefix})
        await ctx.send(
        f"The guild prefix has been set to `{prefix}`. Use `{prefix}prefix [prefix]` to change it again!")

    
def setup(bot):
    bot.add_cog(Config(bot))