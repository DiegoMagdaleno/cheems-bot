import discord
from discord.ext import commands
from lib import token

bot = commands.Bot(command_prefix='>')

@bot.command()
async def ping(ctx):
    await ctx.send('Im rumning from env tokem')

session_token = token.get_token()
bot.run(session_token)