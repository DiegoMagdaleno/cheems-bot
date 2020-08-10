from discord.embeds import Embed
import discord
from discord.ext import commands
from helpers import token, config, reddit, embeds
import os

bot = commands.Bot(command_prefix='>')
config_path = os.path.abspath("config.json")
file_load = open(config_path, 'r').read()

session_config = config.Configuration(file_load)

@bot.command()
async def ping(ctx):
    await ctx.send('Im rumning from env tokem')


@bot.command()
async def meme(ctx):
    reddit_post = reddit.RedditPost(session_config.get_reddit_client_id(), session_config.get_client_secret(), session_config.get_user_agent(), "dogelore")
    await ctx.send(embed=embeds.EmbedMessage(discord.colour.Color.red(), reddit_post.get_post_title(), reddit_post.get_random_meme(), reddit_post.get_post_subreddit(), reddit_post.get_post_author(), reddit_post.get_poster_avatar()).getEmbedMessage())


session_token = token.get_token()
bot.run(session_token)
