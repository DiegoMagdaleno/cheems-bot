import discord
from discord.ext import commands
from helpers import config, embeds, random_operations, fourchan
import os
import sys
import traceback


bot = commands.Bot(command_prefix='>')
config_path = os.path.abspath("config.json")
file_load = open(config_path, 'r').read()

session_config = config.Configuration(file_load)

initial_extensions = ['cogs.fun',
                      'cogs.nekoactions', 'cogs.nsfw', 'cogs.reddit']
if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()


@bot.command()
async def ping(ctx):
    random_cheems = random_operations.get_cheems_phrase()
    await ctx.send(random_cheems)


@bot.command()
async def tech(ctx):
    target_board = 'g'
    fourchan_post = fourchan.FourChanImage(target_board)
    embed_message = embeds.FourChanEmbed(discord.Color.green(
    ), fourchan_post.topic, fourchan_post.image_url, target_board, fourchan_post.url).getEmbedMessage()
    await ctx.send(embed=embed_message)


bot.run(session_config.discord_token)
