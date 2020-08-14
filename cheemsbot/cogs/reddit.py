import os
from discord.ext.commands.core import command
from cheemsbot.helpers import config, reddit, embeds
from discord.ext import commands
import discord

bot = commands.Bot(command_prefix='>')
config_path = os.path.abspath("config.json")
file_load = open(config_path, 'r').read()

session_config = config.Configuration(file_load)

class RedditCommandsCog(commands.Cog, name="Reddit posts and memes"):
    def __init__(self, bot, configuration=None):
        self.bot = bot
        self.session_config = configuration
    
    @commands.command(name='dogememe', aliases=['dgmeme'])
    async def dogememe(self, ctx):
        reddit_post = reddit.RedditPost(self.session_config.reddit_client_id,
        self.session_config.reddit_client_secret,
        self.session_config.reddit_user_agent,
        self.session_config.reddit_user,
        self.session_config.reddit_password,
        "dogelore")
        embed_message = embeds.RedditEmbedMessage(discord.Color.orange(),
        reddit_post.post_title, 
        reddit_post.post_image, 
        reddit_post.post_subreddit,
        reddit_post.post_author,
        reddit_post.post_author_avatar,
        reddit_post.post_link).getEmbedMessage()
        await ctx.send(embed=embed_message)
    
    @commands.command(name="redditmeme", aliases=['rmeme'])
    async def redditmeme(self, ctx, *, subreddit=None):
        self.forbidden = ['cock', 'ass', 'sex', 'dick', 'penis', 'pussy']
        self.current_subreddit = subreddit
        if self.current_subreddit == None:
            await ctx.send("Gimve a sumbreddit")
        else:
            reddit_post = reddit.RedditPost(self.session_config.reddit_client_id,
        self.session_config.reddit_client_secret,
        self.session_config.reddit_user_agent,
        self.session_config.reddit_user,
        self.session_config.reddit_password,
        self.current_subreddit)
            if (reddit_post.is_nsfw) and (ctx.channel.is_nsfw() == False):
                await ctx.send("Not infromt of the childrem")
                return
            self.string_test_result = any(element in self.current_subreddit for element in self.forbidden)
            if self.string_test_result:
                await ctx.send("Ummmm sumbreddit comtains formbidden wormd, somry")
                return
            embed_message = embeds.RedditEmbedMessage(discord.Color.orange(),
            reddit_post.post_title,
            reddit_post.post_image,
            reddit_post.post_subreddit,
            reddit_post.post_author,
            reddit_post.post_author_avatar,
            reddit_post.post_link).getEmbedMessage()
            await ctx.send(embed=embed_message)

def setup(bot):
    bot.add_cog(RedditCommandsCog(bot, session_config))
