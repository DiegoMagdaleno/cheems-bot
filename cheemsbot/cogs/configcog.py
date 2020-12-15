from cheemsbot.helpers.database import IdNotFound
from discord.ext import commands

class Config(commands.Cog, name="Configuration"):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.group(name="prefix", invoke_without_command=True)
    async def prefix_cmd(self, ctx):
        await ctx.channel.send("Base command for setting the prefix, select either: list, add, remove")

    @prefix_cmd.command(name="list")
    async def prefix_cmd_list(self, ctx):
        try:
            data = await self.bot.config.find(ctx.guild.id)
        except IdNotFound:
            await ctx.channel.send("No other prefixes than the default bot prefix have been added")
            return
        await ctx.channel.send(data["prefix"])
    
    @prefix_cmd.command(name="add")
    async def prefix_cmd_add(self, ctx, *, prefix=None):
        if prefix is None:
            await ctx.send("You need to provide a prefix")
            return
        
        if ' ' in prefix:
            await ctx.send("You cant have prefixes with spaces")
            return

        prefix_list = []

        try:
            data = await self.bot.config.find(ctx.guild.id)
            data_prefix_load = data["prefix"]
            for prefixes in data_prefix_load:
                prefix_list.append(prefixes.strip())
        except IdNotFound:
            pass
        
        if prefix in prefix_list and len(prefix_list) > 0:
            await ctx.send("That prefix is already in the database.")
            return

        if len(prefix) > 1:
            target_to_add = f"{prefix} "
        else:
            target_to_add = prefix

        await self.bot.config.upsert({"_id": ctx.guild.id, "prefix": target_to_add}, option="push")
        await ctx.send(
        f"The guild prefix has been set to `{prefix}`. Use `{prefix}prefix [prefix]` to change it again!")

    @prefix_cmd.command(name="remove")
    async def prefix_cmd_remove(self, ctx, *, prefix=None):
        if prefix is None:
            await ctx.send("You need to provide a prefix to remove")
        
        if ' ' in prefix:
            await ctx.send("No spaces")

        try:
            data = await self.bot.config.find(ctx.guild.id)
        except IdNotFound:
            await ctx.send("Cant remove anything because there are no prefixes for this guild")
            return
        
        if len(prefix) > 1:
            target_to_add = f"{prefix} "
        else:
            target_to_add = prefix


        if target_to_add not in data["prefix"]:
            await ctx.send("That prefix is not in the database for this guild")
            return
        else:
            await self.bot.config.upsert({"_id": ctx.guild.id, "prefix": target_to_add}, option="pull")

    
def setup(bot):
    bot.add_cog(Config(bot))