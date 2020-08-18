import discord
from discord import embeds
from discord.embeds import Embed
from discord.ext import commands


class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help")
    async def help(self, ctx, *cog):
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

                    cogs_desc += (
                        "**{}**\n• {}".format(each_cog, self.bot.cogs[each_cog].__doc__)
                        + "\n"
                    )
                our_help_embed.add_field(
                    name="Categories",
                    value=cogs_desc[0 : len(cogs_desc) - 1],
                    inline=True,
                )
                commands_desc = ""
                for command in self.bot.walk_commands():
                    if not command.cog_name and not command.hidden:
                        commands_desc += (
                            "{} - {}".format(command.name, command.help) + "\n"
                        )
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
                        for each in cog:
                            if each_cog == each:
                                our_help_embed = discord.Embed(
                                    title=cog[0] + " Command Listing",
                                    description=self.bot.cogs[cog[0]].__doc__,
                                )
                                for individual_cog in self.bot.get_cog(
                                    each
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
                            description='Are you sure the command"' + cog[0] + '"Exits?',
                            color=discord.Color.red(),
                        )
                    else:
                        await ctx.send(embed=our_help_embed)
        except:
            await ctx.send("Excuse me, I can't send embeds.")


def setup(bot):
    bot.add_cog(HelpCog(bot))

