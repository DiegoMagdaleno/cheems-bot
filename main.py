from discord.embeds import Embed
import discord
from discord.ext import commands
from nekos.nekos import textcat
from helpers import config, reddit, embeds, randomBall, fourchan, nekoimg
import os
import basc_py4chan
import random
import nekos

bot = commands.Bot(command_prefix='>')
config_path = os.path.abspath("config.json")
file_load = open(config_path, 'r').read()

session_config = config.Configuration(file_load)


@bot.command()
async def ping(ctx):
    await ctx.send('Im rumning from env tokem')


@bot.command()
async def dogememe(ctx):
    reddit_post = reddit.RedditPost(session_config.reddit_client_id,
                                    session_config.reddit_client_secret, session_config.reddit_user_agent, session_config.reddit_user, session_config.reddit_password, "dogelore")
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
    embed_message = embeds.FourChanEmbed(discord.Color.green(
    ), fourchan_post.topic, fourchan_post.image_url, target_board, fourchan_post.url).getEmbedMessage()
    await ctx.send(embed=embed_message)


@bot.command()
async def girlfriend(ctx):
    reddit_post = reddit.RedditPost(session_config.reddit_client_id,
                                    session_config.reddit_client_secret, session_config.reddit_user_agent, session_config.reddit_user, session_config.reddit_password, "gentlemanboners")
    await ctx.send(reddit_post.post_image)


@bot.command()
async def boyfriend(ctx):
    reddit_post = reddit.RedditPost(session_config.reddit_client_id,
                                    session_config.reddit_client_secret, session_config.reddit_user_agent, session_config.reddit_user, session_config.reddit_password, "ladyboners")
    await ctx.send(reddit_post.post_image)


# TODO: Here it should be r/femboy, however, we tried to fix it, and it refuses to work.
# it returns a none type, this ofc makes an error, this however should be look up on
# as many users have requested this feature to be r/femboy and not r/crossdressing
# wen eta femboy command :(
@bot.command()
async def femboy(ctx):
    reddit_post = reddit.RedditPost(session_config.reddit_client_id,
                                    session_config.reddit_client_secret, session_config.reddit_user_agent, session_config.reddit_user, session_config.reddit_password,
                                    "crossdressing")
    await ctx.send(reddit_post.post_image)

@bot.command()
async def neko(ctx):
    await ctx.send(nekoimg.get_neko_sfw())

@bot.command()
async def lewdneko(ctx):
    if ctx.channel.is_nsfw():
        await ctx.send(nekoimg.get_neko_nsfw())
    else:
        await ctx.send("Not infromt of the childmren.")

@bot.command()
async def meme(ctx, *, subreddit=None):
    if subreddit == None:
        await ctx.send("Gimve me a sumbreddit")
    else:
            reddit_post = reddit.RedditPost(session_config.reddit_client_id,
                                    session_config.reddit_client_secret, session_config.reddit_user_agent, session_config.reddit_user, session_config.reddit_password,
                                    subreddit)
            embed_message = embeds.RedditEmbedMessage(discord.Color.orange(), reddit_post.post_title, reddit_post.post_image,
                                              reddit_post.post_subreddit, reddit_post.post_author, reddit_post.post_author_avatar, reddit_post.post_link).getEmbedMessage()
            await ctx.send(embed=embed_message)

@bot.command()
async def owofy(ctx, *, text=None):
    if text == None:
         await ctx.send("Gimve me a memsage")
    else:
        await ctx.send(nekoimg.owo_text(text))

bot.run(session_config.discord_token)
