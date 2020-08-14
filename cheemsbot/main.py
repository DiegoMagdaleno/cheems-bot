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
                      'cogs.nekoactions', 'cogs.nsfw', 'cogs.reddit', 'cogs.fourchan', 'cogs.root', 'cogs.moderation']
if __name__ == '__main__':
    bot.remove_command('help')
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()


bot.run(session_config.discord_token)
