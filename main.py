from discord.embeds import Embed
import discord
from discord.ext import commands
from helpers import token, config, reddit, embeds

bot = commands.Bot(command_prefix='>')
Reddit_session = reddit.RedditPost("dogelore")


@bot.command()
async def ping(ctx):
    await ctx.send('Im rumning from env tokem')


@bot.command()
async def meme(ctx):
    await ctx.send(embed=embeds.EmbedMessage(discord.colour.Color.red(), Reddit_session.get_post_title(), Reddit_session.get_random_meme(), Reddit_session.get_post_subreddit(), Reddit_session.get_post_author(), Reddit_session.get_poster_avatar()).getEmbedMessage())


session_token = token.get_token()
bot.run(session_token)
