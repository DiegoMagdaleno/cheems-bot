from discord.embeds import Embed
import discord
from discord.ext import commands
from helpers import config, reddit, embeds, randomBall, fourchan
import os
import basc_py4chan
import random

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
    embed_message = embeds.RedditEmbedMessage(discord.Color.orange(), reddit_post.post_title, reddit_post.post_image,
                                        reddit_post.post_subreddit, reddit_post.post_author, reddit_post.post_author_avatar, reddit_post.post_link).getEmbedMessage()
    await ctx.send(embed=embed_message)


@bot.command()
async def ask(ctx, *, question=None):
    if question == None:
        await ctx.send("I meed you to amsk somethimg")
    else:
        ask_answer = randomBall.get_8_ball()
        await ctx.send(f"{ctx.author.mention}, "+ask_answer)

@bot.command()
async def tech(ctx):
    target_board = 'g'
    fourchan_post = fourchan.FourChanImage(target_board)
    embed_message = embeds.FourChanEmbed(discord.Color.green(), fourchan_post.topic, fourchan_post.image_url, target_board, fourchan_post.url).getEmbedMessage()
    await ctx.send(embed=embed_message)

@bot.command()
async def girlfriend(ctx):
    reddit_post = reddit.RedditPost(session_config.reddit_client_id,
                                    session_config.reddit_client_secret, session_config.reddit_user_agent, "gentlemanboners")
    await ctx.send(reddit_post.post_image)

bot.run(session_config.discord_token)
