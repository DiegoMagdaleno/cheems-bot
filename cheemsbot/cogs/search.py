import discord
from discord.ext import commands
import requests
import datetime

bot = commands.Bot(command_prefix=">")


class SearchUtilitiesCog(commands.Cog, name="Search"):
    """A collection of commands to help you search without leaving Discord"""

    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(name="wikipedia")
    async def wikipedia(self, ctx, *, query):
        self.search = requests.get(
            (
                "https://en.wikipedia.org//w/api.php?action=query"
                "&format=json&list=search&utf8=1&srsearch={}&srlimit=5&srprop="
            )
            .format(query)
        ).json()["query"]

        if self.search["searchinfo"]["totalhits"] == 0:
            await ctx.send("Ummm I coulmdnt find anything")
            return
        for each_search in range(len(self.search["search"])):
            self.article = self.search["search"][each_search]["title"]
            self.request = requests.get(
                (
                    "https://en.wikipedia.org//w/api.php?action=query"
                    "&utf8=1&redirects&format=json&prop=info|images"
                    "&inprop=url&titles={}"
                ).format(self.article)
            ).json()["query"]["pages"]
            if str(list(self.request)[0]) != "-1":
                break
            else:
                await ctx.send("Ummm I coulmdnt find anything")
                return
        self.artic = self.request[list(self.request)[0]]["title"]
        self.artic_url = self.request[list(self.request)[0]]["fullurl"]
        self.artic_desc = requests.get(
            "https://en.wikipedia.org/api/rest_v1/page/summary/{}".format(self.artic)
        ).json()["extract"]
        self.last_edit = datetime.datetime.strptime(
            self.request[list(self.request)[0]]["touched"], "%Y-%m-%dT%H:%M:%SZ"
        )
        self.our_embed = discord.Embed(
            title="**{}**".format(self.artic),
            url=self.artic_url,
            description=self.artic_desc,
            color=discord.Color.magenta(),
        )
        self.our_embed.set_footer(
            text="Wiki entry last modified",
            icon_url="https://upload.wikimedia.org/wikipedia/commons/6/63/Wikipedia-logo.png",
        )
        self.our_embed.set_author(
            name="Wikipedia",
            url="https://en.wikipedia.org/",
            icon_url="https://upload.wikimedia.org/wikipedia/commons/6/63/Wikipedia-logo.png",
        )
        self.our_embed.timestamp = self.last_edit
        await ctx.send('**Search result for:** ***"{}"***:'.format(query), embed=self.our_embed)

def setup(bot):
    bot.add_cog(SearchUtilitiesCog(bot))
