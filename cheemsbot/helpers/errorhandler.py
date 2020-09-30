import discord


class BotAlert:
    def __init__(self, type: int, why: str):
        self.type = type
        self.why = why

    def get_error_embed(self):
        # Type levels:
        # 0 - Succesfull operation
        # 1 - Warning
        # 2 - Error
        self.embed = discord.Embed()
        if self.type == 0:
            self.why = ":white_check_mark: " + self.why
            self.embed.color = discord.Color.green()
            self.embed.title = "Operation was completed successfully!"
            self.embed.description = self.why
            return self.embed
        if self.type == 1:
            self.why = ":warning: " + self.why
            self.embed.color = discord.Color.gold()
            self.embed.title = "Warning"
            self.embed.description = self.why
            return self.embed
        if self.type >= 2:
            self.why = ":x: " + self.why
            self.embed.color = discord.Color.red()
            self.embed.title = "Critical error"
            self.embed.description = self.why
            return self.embed
