

import discord
from discord.ext import commands
from cheemsbot.helpers.paginator import LinePaginator

class CreditsCog(commands.Cog, name="Credits"):
    def __init__(self, bot) -> None:
        self.bot = bot
    

    @commands.command(name="libraries")
    async def libraries(self, ctx):
        self.lines = ["**Discord.py** - Interactions with Discord, like sending messages, embeds.", "**PRAW** - Grabbing information from Reddit!", "**Nekos.py** - Getting anime images", "**basc_py4chan** - Interactions with 4chan", "**lmgtify_reborn** - Getting lmgtify URLS", "**GoogleImageSearch** - Getting Image search results from Google!", "**Loguru** - Internal logging and debugging", "**Beatifulsoup4** - Website scrapping", "**Switch** - Switch case for Python"]
        embed = discord.Embed()
        embed.set_author(name="Cheems uses the following libraries:", url="https://whatever.com", icon_url="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png")
        await LinePaginator.paginate(
            lines=(line for line in self.lines),
            ctx=ctx, embed=embed, bot=self.bot, max_lines=1, max_size=100)
    
    @commands.command(name="authors")
    async def authors(self, ctx):
        self.lines = ["**Diego Magdaleno** - Main bot author", "**Stkc** - Neko actions implementation", "**Clyde** - Ping in ms", "**Luth** - Testing"]
        embed = discord.Embed()
        embed.set_author(name="Cheems was made by the following people!", url="https://whatever.com", icon_url="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png")
        await LinePaginator.paginate(
            lines=(line for line in self.lines),
            ctx=ctx, embed=embed, bot=self.bot, max_lines=1, max_size=100)
def setup(bot):
    bot.add_cog(CreditsCog(bot))