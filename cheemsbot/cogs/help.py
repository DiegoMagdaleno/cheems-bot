import discord
from discord import embeds
from discord.ext import commands
from cheemsbot.helpers import errorhandler


class HelpCog(commands.Cog):
    """Internal cog that handles help operations"""

    def __init__(self, bot):
        self.bot = bot
        self.hidden = True

    @commands.command(name="help", hidden=True)
    async def help(self, ctx, *cog):
        """Displays the help message what else"""
        try:
            if not cog:
                our_help_embed = discord.Embed(
                    title="🍔 Cheemsburbger help",
                    description="Cheems advanced technologies",
                    color=discord.Color.green(),
                )
                our_help_embed.set_thumbnail(
                    url="https://media.discordapp.net/attachments/743930523440775253/744976899037593710/3dgifmaker71.gif"
                )
                our_help_embed.set_footer(
                    text="Cheemsburguer is free software. And it is licensed under the WTFPL license. Copyright Diego Magdaleno 2020 et al."
                )
                cogs_desc = ""

                for each_cog in self.bot.cogs:

                    if vars(self.bot.cogs[each_cog]).get("hidden") is not True:
                        cogs_desc += (
                            f"**{each_cog}**\n• {self.bot.cogs[each_cog].__doc__}\n"
                        )
                our_help_embed.add_field(
                    name="Categories",
                    value=cogs_desc[0 : len(cogs_desc) - 1],
                    inline=True,
                )
                commands_desc = ""
                for command in self.bot.walk_commands():
                    if not command.cog_name and not command.hidden:
                        commands_desc += f"{command.name} - {command.help}\n"
                if commands_desc != "":
                    our_help_embed.add_field(
                        name="Uncategorized commands",
                        value=commands_desc[0 : len(commands_desc) - 1],
                        inline=False,
                    )
                await ctx.send(embed=our_help_embed)
            else:
                if len(cog) > 1:
                    our_help_embed = discord.Embed(
                        title="Error!",
                        description="Too many cogs",
                        color=discord.Color.red(),
                    )
                    await ctx.send(embed=our_help_embed)
                else:
                    found = False
                    for each_cog in self.bot.cogs:
                        index_target = [x.lower() for x in self.bot.cogs.keys()].index(cog[0].lower())
                        to_lower = each_cog.lower()
                        for each in cog:
                            if to_lower == each.lower():
                                target = list(self.bot.cogs.keys())[index_target]
                                our_help_embed = discord.Embed(
                                    title=target+ " Command Listing",
                                    description=self.bot.cogs[target].__doc__,
                                )
                                for individual_cog in self.bot.get_cog(
                                    target
                                ).get_commands():
                                    if not individual_cog.hidden:
                                        our_help_embed.add_field(
                                            name=individual_cog.name,
                                            value=individual_cog.help,
                                            inline=False,
                                        )
                                        found = True
                    if not found:
                        our_help_embed = discord.Embed(
                            title="Error!",
                            description='Are you sure the command"'
                            + cog[0]
                            + '"Exits?',
                            color=discord.Color.red(),
                        )
                    else:
                        await ctx.send(embed=our_help_embed)
        except:
            await ctx.send(
                embed=errorhandler.BotAlert(
                    2, "Excuse me, I can't send embeds."
                ).get_error_embed()
            )


def setup(bot):
    bot.add_cog(HelpCog(bot))
