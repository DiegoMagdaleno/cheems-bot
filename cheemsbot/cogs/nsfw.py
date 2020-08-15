from discord.ext.commands.core import command
from cheemsbot.helpers import config, reddit, nekoimg
from discord.ext import commands
import os

bot = commands.Bot(command_prefix=">")

bot = commands.Bot(command_prefix=">")
config_path = os.path.abspath("config.json")
file_load = open(config_path, "r").read()

session_config = config.Configuration(file_load)


class NSFWCommandsCog(commands.Cog, name="NSFW"):
    def __init__(self, bot, configuration=None) -> None:
        self.bot = bot
        self.session_config = configuration

    @commands.command(name="lewdfemboy")
    async def lewdfemboy(self, ctx):
        if ctx.channel.is_nsfw():
            reddit_post = reddit.RedditPost(
                self.session_config.reddit_client_id,
                self.session_config.reddit_client_secret,
                self.session_config.reddit_user_agent,
                self.session_config.reddit_user,
                self.session_config.reddit_password,
                "femboys",
            )
            await ctx.send(reddit_post.post_image)
        else:
            await ctx.send("Not infromt of the childmren.")

    @commands.command(name="lewdneko")
    async def lewdneko(self, ctx):
        if ctx.channel.is_nsfw():
            await ctx.send(nekoimg.get_neko_nsfw())
        else:
            await ctx.send("Not infromt of the childmren.")


def setup(bot):
    bot.add_cog(NSFWCommandsCog(bot, session_config))
