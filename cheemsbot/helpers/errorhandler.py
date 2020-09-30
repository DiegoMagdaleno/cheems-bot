
import discord


class BotAlert():
    def __init__(self, type: int, why: str):
        self.type = type
        self.why = why
    
    def get_error_embed(self):
        # Type levels:
            # 0 - Succesfull operation
            # 1 - Warning
            # 2 - Error
        self.embed = discord.Embed()
        self.embed.description = self.why
        if self.type == 0:
            self.embed.color = discord.Color.green()
            self.embed.title = "Operation was completed successfully!"
            return self.embed
        if self.type == 1:
            self.embed.color = discord.Color.gold()
            self.embed.title = "Warning"
            return self.embed
        if self.type >= 2:
            self.embed.color = discord.Color.red()
            self.embed.title = "Critical error"
            return self.embed
            

