from helpers import config
import discord
from discord.ext import commands
from cheemsbot.helpers import reddit, config
import os

bot = commands.Bot(command_prefix='>')
config_path = os.path.abspath("config.json")
file_load = open(config_path, 'r').read()

session_config = config.Configuration(file_load)

class FunWithCheemsCog(commands.Cog, name="Fun with cheemsburger"):
    def __init__(self, bot, configuration=None):
        self.bot = bot
        self.session_config = configuration

    @commands.command(name='gf')
    async def girlfriend(self, ctx):
        reddit_post = reddit.RedditPost(self.session_config.reddit_client_id,
                                        self.session_config.reddit_client_secret, self.session_config.reddit_user_agent, self.session_config.reddit_user, self.session_config.reddit_password, "gentlemanboners")
        await ctx.send(reddit_post.post_image)

def setup(bot):
    bot.add_cog(FunWithCheemsCog(bot, session_config))