import cheemsbot.config as conf
from cheemsbot.helpers import nekoimg
from cheemsbot.helpers import errorhandler


from discord.ext import commands


class NSFWCommandsCog(commands.Cog, name="NSFW"):
    """Actions that can only be run on NSFW channels. Contains adult content."""

    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(name="lewdfemboy")
    async def lewdfemboy(self, ctx):
        """Description:  Grabs an image from r/femboys and shows it to the user.\nArguments: `None`"""
        if ctx.channel.is_nsfw():
            self.reddit_post = conf.get_reddit_post("femboys")
            await ctx.send(self.reddit_post.image)
        else:
            await ctx.send(
                embed=errorhandler.BotAlert("error", "Can't post NSFW in non-NSFW channels."
                ).get_error_embed()
            )

    @commands.command(name="lewdneko")
    async def lewdneko(self, ctx):
        """Description: Grabs a hentai image or gif and it gets displayed.\nArguments: `None`"""
        async with ctx.typing():
            if ctx.channel.is_nsfw():
                await ctx.send(nekoimg.get_neko_nsfw())
            else:
                await ctx.send(
                    embed=errorhandler.BotAlert(
                        2, "Can't post NSFW in non-NSFW channels."
                    ).get_error_embed()
                )


def setup(bot):
    bot.add_cog(NSFWCommandsCog(bot))
