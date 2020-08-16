import cheemsbot.config as conf
from cheemsbot.helpers import nekoimg

from discord.ext import commands


class NSFWCommandsCog(commands.Cog, name="NSFW"):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(name="lewdfemboy")
    async def lewdfemboy(self, ctx):
        if ctx.channel.is_nsfw():
            self.reddit_post = conf.get_reddit_post("femboys")
            await ctx.send(self.reddit_post.post_image)
        else:
            await ctx.send("Not infromt of the childmren.")

    @commands.command(name="lewdneko")
    async def lewdneko(self, ctx):
        async with ctx.typing():
            if ctx.channel.is_nsfw():
                await ctx.send(nekoimg.get_neko_nsfw())
            else:
                await ctx.send("Not infromt of the childmren.")


def setup(bot):
    bot.add_cog(NSFWCommandsCog(bot))
