from discord.embeds import Embed
import discord
from discord.ext import commands
from helpers import config, reddit, embeds
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
    reddit_post = reddit.RedditPost(session_config.reddit_client_id,
                                    session_config.reddit_client_secret, session_config.reddit_user_agent, "dogelore")
    embed_message = embeds.EmbedMessage(discord.colour.Color.blue(), reddit_post.post_title, reddit_post.post_image,
                                        reddit_post.post_subreddit, reddit_post.post_author, reddit_post.post_author_avatar, reddit_post.post_link).getEmbedMessage()
    await ctx.send(embed=embed_message)

bot.run(session_config.discord_token)
