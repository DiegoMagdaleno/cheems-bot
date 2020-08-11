from discord.ext.commands.core import command
from cheemsbot.helpers import nekoimg, embeds
from discord.ext import commands
import discord

bot = commands.Bot(command_prefix='>')


class NekoActionCog(commands.Cog, name="Neko actions"):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.our_neko_actions = nekoimg.NekoActions()

    @commands.command(name='cuddle')
    async def cuddle(self, ctx, member: discord.User = None):
        self.current_member = member
        if self.current_member == None:
            await ctx.send("Gimve me a user")
        else:
            neko_action = embeds.NekoEmbed(discord.Color.blurple(),
                                           self.our_neko_actions.neko_cuddle(),
                                           ctx.author.name,
                                           str(member.name),
                                           'cuddle').getEmbedMessage()
        await ctx.send(embed=neko_action)

    @commands.command(name='pat')
    async def headpat(self, ctx, member: discord.User = None):
        self.current_member = member
        if self.current_member == None:
            await ctx.send("Gimve me a user")
        else:
            neko_action = embeds.NekoEmbed(discord.Color.blurple(),
                                           self.our_neko_actions.neko_pat(),
                                           ctx.author.name,
                                           str(member.name),
                                           'pat').getEmbedMessage()
        await ctx.send(embed=neko_action)

    @commands.command(name='kiss')
    async def kiss(self, ctx, member: discord.User = None):
        self.current_member = member
        if self.current_member == None:
            await ctx.send("Gimve me a user")
        else:
            neko_action = embeds.NekoEmbed(discord.Color.blurple(),
                                           self.our_neko_actions.neko_kiss(),
                                           ctx.author.name,
                                           str(member.name),
                                           'kiss').getEmbedMessage()
        await ctx.send(embed=neko_action)

    @commands.command(name='slap')
    async def slap(self, ctx, member: discord.User = None):
        self.current_member = member
        if self.current_member == None:
            await ctx.send("Gimve me a user")
        else:
            neko_action = embeds.NekoEmbed(discord.Color.blurple(),
                                           self.our_neko_actions.neko_slap(),
                                           ctx.author.name,
                                           str(member.name),
                                           'slap').getEmbedMessage()
        await ctx.send(embed=neko_action)


def setup(bot):
    bot.add_cog(NekoActionCog(bot))
