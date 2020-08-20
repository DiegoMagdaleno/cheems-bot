from cheemsbot.helpers import animals

from discord.ext import commands


class AnimalCommandCog(commands.cog, name="Animals"):
    """Set of actions to get some flufy animals from the internet into Discord chat"""

    def __init__(self, bot ) -> None:
        self.bot = bot

    @commands.command(name="shiba")
    async def shiba(self, ctx):
        """Description: Gets an image from Shibas.online api and posts it in chat\nArguments:`none`"""
        self.our_shiba = animals.Animals.shiba()
        await ctx.send(self.our_shiba)
    
    @commands.command(name="cat")
    async def cat(self, ctx):
        """Description: Gets a cat image and posts it in chat\nArguments:`none`"""
        self.our_cat = animals.Animals.cat()
        await ctx.send(self.our_cat)
    
    @commands.command(name="dog")
    async def dog(self, ctx):
        """Description: Gets a dog image and posts it in chat\nArguments:`none`"""
        self.our_dog = animals.Animals.dog()
        await ctx.send(self.our_dog)

def setup(bot):
    bot.add_cog(AnimalCommandCog(bot))