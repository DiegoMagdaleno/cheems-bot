from discord.ext import commands
import discord
from cheemsbot.helpers import random_operations


class CheemsRootCommandsCog(commands.Cog, name="Root"):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="help")
    async def help(self, ctx):
        self.embed = discord.Embed(
            title="Cheems advanced technologies",
            description="Official help sheet",
            color=0x00FF7B,
        )
        self.embed.set_author(
            name="Cheemsburguer help",
            icon_url="https://cdn140.picsart.com/314611123258211.png?type=webp&to=min&r=480",
        )
        self.embed.add_field(name="4chan", value="tech", inline=False)
        self.embed.add_field(
            name="Fun with cheemsburguer",
            value="ask, bf, femboy, gf, ischad, neko, owofy",
            inline=False,
        )
        self.embed.add_field(name="NSFW", value="lewdfemboy, lewdneko", inline=True)
        self.embed.add_field(
            name="Neko Actions", value="cuddle, kiss, pat, slap", inline=True
        )
        self.embed.add_field(name="Reddit", value="dogememe, redditmeme", inline=True)
        self.embed.add_field(name="Root ", value="help, ping", inline=True)
        self.embed.set_footer(
            text="Cheemsburguer is free software. And it is licensed under the WTFPL license. Copyright Diego Magdaleno 2020 et al."  # noqa: E501
        )
        await ctx.send(embed=self.embed)

    @commands.command(name="ping")
    async def ping(self, ctx):
        self.random_cheems = random_operations.get_cheems_phrase()
        await ctx.send(
            self.random_cheems + " \n**Pimg:** {0}".format((round(self.bot.latency, 1)))
        )


def setup(bot):
    bot.add_cog(CheemsRootCommandsCog(bot))
