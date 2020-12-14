from logging import exception

from discord.ext import commands
import discord

import cheemsbot.config as conf
from cheemsbot.helpers import database, errorhandler

import asyncio

from loguru import logger as log
import os

import motor.motor_asyncio

bot = commands.Bot(command_prefix=">", case_insensitive=True)

file_base = os.path.dirname(os.path.realpath(__file__))

@bot.event
async def on_command_error(ctx: commands.Context, error: commands.errors):
    if isinstance(error, commands.CommandOnCooldown):
        await (
            await ctx.send(
                embed=errorhandler.BotAlert(
                    "warn",
                    f"This command is in a {error.retry_after :.2f} cooldown, try again later",
                ).get_error_embed()
            )
        ).delete(delay=5)
        await asyncio.sleep(6)
    if isinstance(error, commands.CommandNotFound):
        await (
            await ctx.send(
                embed=errorhandler.BotAlert(
                    "warn", "That command isn't in my command list!"
                ).get_error_embed()
            )
        ).delete(delay=5)
        await asyncio.sleep(6)
    if isinstance(error, errorhandler.CommandRedditBreaker):
        await (
            await ctx.send(
                embed=errorhandler.BotAlert(
                    "error",
                    "There was an error fetching that Subreddit! Are you sute it exists and it isn't banned from Reddit?",
                ).get_error_embed()
            )
        ).delete(delay=5)
        await asyncio.sleep(6)
    if isinstance(error, commands.CommandInvokeError):
        await (
            await ctx.send(
                embed=errorhandler.BotAlert(
                    type="error",
                    why="There was an error running this command. Internal bot error!.",
                ).get_error_embed()
            )
        ).delete(delay=5)
        await asyncio.sleep(6)
    raise error


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Eating a Cheemsburbger"))

    log.info("Cheems bot is ready to run!")

    try:
        await bot.config.get_all()
    except database.PyMongoError as e:
        log.error(f"An error ocurred fetching the config {e}")
    else:
        log.info("Database connection has been stablished!")

if __name__ == "__main__":
    bot.db = motor.motor_asyncio.AsyncIOMotorCliet(conf.mongo_url)

    bot.config = database.DocumentInteractor(bot.db, "config")

    for extension in os.listdir(f"{file_base}/cogs"):
        if extension.endswith(".py") and not extension.startswith("_"):
            try:
                bot.load_extension(extension)
            except Exception as e:
                log.error(
                    f"An error ocurred while loading the extension {extension}, the following error was reported: {e}."
                )
    log.debug("Cheems is ready to run")
    log.debug(f"The following extensions were succesfully loaded {bot.cogs}")

    bot.remove_command("help") # Remove default help command
    bot.run(conf.our_discord_token)
