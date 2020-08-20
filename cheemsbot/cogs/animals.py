from discord.ext.commands.core import command
from cheemsbot.helpers import animals
import cheemsbot.config as conf


from discord.ext import commands


class AnimalCommandCog(commands.Cog, name="Animals"):
    """Set of actions to get some flufy animals from the internet into Discord chat"""

    def __init__(self, bot ) -> None:
        self.bot = bot
        self.animal_session = animals.Animals()

    @commands.command(name="shiba")
    async def shiba(self, ctx):
        """Description: Gets an image from Shibas.online api and posts it in chat\nArguments: `none`"""
        self.our_shiba = self.animal_session.shiba()
        await ctx.send(self.our_shiba)
    
    @commands.command(name="cat")
    async def cat(self, ctx):
        """Description: Gets a cat image and posts it in chat\nArguments: `none`"""
        self.our_cat = self.animal_session.cat()
        await ctx.send(self.our_cat)
    
    @commands.command(name="dog")
    async def dog(self, ctx):
        """Description: Gets a dog image and posts it in chat\nArguments: `none`"""
        self.our_dog = self.animal_session.dog()
        await ctx.send(self.our_dog)
    
    @commands.command(name="rat")
    async def rat(self, ctx):
        """Description: Grabs an image from r/RATS and posts it in chat\nArguments: `none`"""
        self.reddit_post = conf.get_reddit_post("RATS", True)
        await ctx.send(self.reddit_post.image)
    
    @commands.command(name="fox")
    async def fox(self, ctx):
        """Description: Gets an image from randomfox.ca api and posts it in chat\nArguments: `none`"""
        self.our_fox = self.animal_session.fox()
        await ctx.send(self.our_fox)

def setup(bot):
    bot.add_cog(AnimalCommandCog(bot))