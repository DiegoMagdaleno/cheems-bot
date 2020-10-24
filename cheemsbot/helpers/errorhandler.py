import discord
from discord.ext.commands import CommandError


class CommandRedditBreaker(CommandError):
    def __init__(self, reason) -> None:
        self.reason = reason

        super().__init__(
            f"The following error ocurred {self.reason} when trying to get the subreddit you requested."
        )

class BotAlert:
    def __init__(self, type: str, why: str):
        self.type = type
        self.why = why

    def get_error_embed(self):
        # Type levels:
        # 0 - Succesfull operation
        # 1 - Warning
        # 2 - Error
        self.embed = discord.Embed()
        self.embed.set_footer(text="Cheemsburbger by Diego Magadaleno")
        if self.type == "success":
            self.why = ":white_check_mark: " + self.why
            self.embed.color = discord.Color.green()
            self.embed.title = "Operation was completed successfully!"
            self.embed.description = self.why
            return self.embed
        if self.type == "warn":
            self.why = ":warning: " + self.why
            self.embed.color = discord.Color.gold()
            self.embed.title = "Warning"
            self.embed.description = self.why
            return self.embed
        if self.type == "error":
            self.why = ":x: " + self.why
            self.embed.color = discord.Color.red()
            self.embed.title = "Critical error"
            self.embed.description = self.why
            return self.embed
