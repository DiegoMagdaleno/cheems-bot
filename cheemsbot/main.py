import sys
import traceback

from discord.ext import commands

import cheemsbot.config as conf

bot = commands.Bot(command_prefix=">")

initial_extensions = [
    "cogs.fun",
    "cogs.nekoactions",
    "cogs.nsfw",
    "cogs.reddit",
    "cogs.fourchan",
    "cogs.root",
]
if __name__ == "__main__":
    bot.remove_command("help")
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception:
            print(f"Failed to load extension {extension}.", file=sys.stderr)
            traceback.print_exc()


@bot.event
async def on_command_error(ctx: commands.Context, error: commands.errors):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(
            "Thims command is on a %.2fs coolmdown, trym amgain lamter"
            % error.retry_after
        )
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Ummmmmmmmmmmmm I couldmt fimd that command")
    raise error


bot.run(conf.our_discord_token)
