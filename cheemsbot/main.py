import sys

from discord.ext import commands

import cheemsbot.config as conf

import asyncio

from loguru import logger as log

bot = commands.Bot(command_prefix=">", case_insensitive=True)

initial_extensions = [
    "cogs.help",
    "cogs.fun",
    "cogs.nekoactions",
    "cogs.nsfw",
    "cogs.reddit",
    "cogs.fourchan",
    "cogs.root",
    "cogs.search",
    "cogs.animals",
    "cogs.credits",
]


if __name__ == "__main__":
    bot.remove_command("help")
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception:
            log.critical(f"Failed to load extension {extension}.")

@bot.event
async def on_command_error(ctx: commands.Context, error: commands.errors):    
    if isinstance(error, commands.CommandOnCooldown):
        await (
            await ctx.send(
                "Thims command is on a %.2fs coolmdown, trym amgain lamter"
                % error.retry_after
            )
        ).delete(delay=3)
        await asyncio.sleep(4)
    if isinstance(error, commands.CommandNotFound):
        await (await ctx.send("Ummmmmmmmmmmmm I couldmt fimd that command")).delete(
            delay=3
        )
        await asyncio.sleep(4)
    if isinstance(error, commands.CommandInvokeError):
        await (
            await ctx.send(
                "Ummmm there wams am emrror on thims command, prombably some bamd api response."
            )
        ).delete(delay=3)
        await asyncio.sleep(4)
    raise error

@bot.event
async def on_ready():
    log.debug("Cheems is ready to run.")
    log.debug(f" The following cogs were loaded loadead {bot.cogs}")



bot.run(conf.our_discord_token)
