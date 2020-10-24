from cheemsbot.helpers import embeds
from cheemsbot.helpers import nekoimg
from cheemsbot.helpers import errorhandler

import discord
from discord.ext import commands


class NekoActionCog(commands.Cog, name="NekoActions"):
    """Displays a Neko gif performing some action a desired user"""

    def __init__(self, bot) -> None:
        self.bot = bot
        self.our_neko_actions = nekoimg.NekoActions()

    @commands.command(name="cuddle")
    async def cuddle(self, ctx, member: discord.User = None):
        """Description:  Displays a gif of two anime characters cudling, with a title formatted as User A is cuddling with User B\nArguments: `1`"""
        self.current_member = member
        if self.current_member is None:
            await ctx.send(
                embed=errorhandler.BotAlert("warn", "You need to provide an user."
                ).get_error_embed()
            )
        else:
            if ctx.message.author == member:
                await ctx.send(
                    embed=errorhandler.BotAlert(
                        1, "You can't cuddle with yourself"
                    ).get_error_embed()
                )
                return
            neko_action = embeds.NekoEmbed(
                self.our_neko_actions.neko_cuddle(),
                ctx.author.name,
                str(member.name),
                "cuddle",
            ).get_embed_message()
            await ctx.send(embed=neko_action)

    @commands.command(name="pat")
    async def headpat(self, ctx, member: discord.User = None):
        """Description:  Displays a gif of one anime character patting the other, with a title formatted as User A is patting User B\nArguments: `1`"""
        self.current_member = member
        if self.current_member is None:
            await ctx.send(
                embed=errorhandler.BotAlert("warn", "You need to provide an user."
                ).get_error_embed()
            )
        else:
            if ctx.message.author == self.current_member:
                await ctx.send(
                    embed=errorhandler.BotAlert(
                        1, "You can't pat yourself."
                    ).get_error_embed()
                )
                return
            neko_action = embeds.NekoEmbed(
                self.our_neko_actions.neko_pat(),
                ctx.author.name,
                str(member.name),
                "pat",
            ).get_embed_message()
            await ctx.send(embed=neko_action)

    @commands.command(name="kiss")
    async def kiss(self, ctx, member: discord.User = None):
        """Description:  Displays a gif of two anime characters kissing with a title formatted as User A is kissing User B\nArguments: `1`"""
        self.current_member = member
        if self.current_member is None:
            await ctx.send(
                embed=errorhandler.BotAlert("warn", "You need to provide an user."
                ).get_error_embed()
            )
        else:
            if ctx.message.author == self.current_member:
                await ctx.send(
                    embed=errorhandler.BotAlert(
                        1, "You can't kiss yourself."
                    ).get_error_embed()
                )
                return
            neko_action = embeds.NekoEmbed(
                self.our_neko_actions.neko_kiss(),
                ctx.author.name,
                str(member.name),
                "kiss",
            ).get_embed_message()
            await ctx.send(embed=neko_action)

    @commands.command(name="slap")
    async def slap(self, ctx, member: discord.User = None):
        """Description:  Displays a gif of one anime character slapping another, with a title formatted as User A is slapping User B\nArguments: `1`"""
        self.current_member = member
        if self.current_member is None:
            await ctx.send(
                embed=errorhandler.BotAlert("warn", "You need to provide an user."
                ).get_error_embed()
            )
        else:
            if ctx.message.author == self.current_member:
                await ctx.send(
                    embed=errorhandler.BotAlert(
                        1, "You can't slap yourself"
                    ).get_error_embed()
                )
                return
            neko_action = embeds.NekoEmbed(
                self.our_neko_actions.neko_slap(),
                ctx.author.name,
                str(member.name),
                "slap",
            ).get_embed_message()
            await ctx.send(embed=neko_action)

    @commands.command(name="hug")
    async def hug(self, ctx, member: discord.User = None):
        """Description:  Displays a gif of two anime characters hugging, with a title formatted as User A is hugging User B\nArguments: `1`"""
        self.current_member = member
        if self.current_member is None:
            await ctx.send(
                embed=errorhandler.BotAlert("warn", "You need to provide an user."
                ).get_error_embed()
            )
        else:
            if ctx.message.author == self.current_member:
                await ctx.send(
                    embed=errorhandler.BotAlert(
                        1, "You can't hug yourself"
                    ).get_error_embed()
                )
                return
            neko_action = embeds.NekoEmbed(
                self.our_neko_actions.neko_hug(),
                ctx.author.name,
                str(member.name),
                "hug",
            ).get_embed_message()
            await ctx.send(embed=neko_action)

    @commands.command(name="tickle")
    async def tickle(self, ctx, member: discord.User = None):
        """Description:  Displays a gif of one anime character tickling another, with a title formatted as User A tickling User B\nArguments: `1`"""
        self.current_member = member
        if self.current_member is None:
            await ctx.send(
                embed=errorhandler.BotAlert("warn", "You need to provide an user."
                ).get_error_embed()
            )
        else:
            if ctx.message.author == self.current_member:
                await ctx.send(
                    embed=errorhandler.BotAlert(
                        1, "You can't tickle yourself"
                    ).get_error_embed()
                )
                return
            neko_action = embeds.NekoEmbed(
                self.our_neko_actions.neko_tickle(),
                ctx.author.name,
                str(member.name),
                "tickle",
            ).get_embed_message()
            await ctx.send(embed=neko_action)


def setup(bot):
    bot.add_cog(NekoActionCog(bot))
