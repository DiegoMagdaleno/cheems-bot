import sys

from discord.ext import commands

import cheemsbot.config as conf
from cheemsbot.helpers import errorhandler

import asyncio

from loguru import logger as log
import traceback
import os


bot = commands.Bot(command_prefix=">", case_insensitive=True)

file_base = os.path.dirname(os.path.realpath(__file__))
file_list = os.listdir(f"{file_base}/cogs")
initial_extensions = []
[file_list.remove(item) for item in ["__init__.py", "__pycache__", ".mypy_cache"]]
[initial_extensions.append(f"cogs.{cog.replace('.py', '')}") for cog in file_list]


@bot.event
async def on_command_error(ctx: commands.Context, error: commands.errors):
    if isinstance(error, commands.CommandOnCooldown):
        await (
            await ctx.send(
                embed=errorhandler.BotAlert(
                    1,
                    f"This command is in a {error.retry_after :.2f} cooldown, try again later",
                ).get_error_embed()
            )
        ).delete(delay=3)
        await asyncio.sleep(4)
    if isinstance(error, commands.CommandNotFound):
        await (
            await ctx.send(
                embed=errorhandler.BotAlert(
                    1, "That command isn't in my command list!"
                ).get_error_embed()
            )
        ).delete(delay=3)
        await asyncio.sleep(4)
    if isinstance(error, commands.CommandInvokeError):
        await (
            await ctx.send(
                embed=errorhandler.BotAlert(
                    2, "There was an error running this command. Internal bot error!."
                ).get_error_embed()
            )
        ).delete(delay=3)
        await asyncio.sleep(4)
    raise error


@bot.event
async def on_ready():
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception:
            print(f"Failed to load extension {extension}.", file=sys.stderr)
            traceback.print_exc()
    log.debug("Cheems is ready to run.")
    log.debug(f" The following cogs were loaded loadead {bot.cogs}")


bot.remove_command("help")
bot.run(conf.our_discord_token)
