from discord.ext import commands
import markovify


class GeneratorCog(commands.Cog, name="Generator"):
    @commands.command(name="logger")
    async def log(self, ctx):
        messages = await ctx.channel.history(limit=2000).flatten()
        for i, message in enumerate(messages):
            message = message.content
            file = open("data.txt", "a")
            print(i)
            file.write(message + "\n")
            file.close()

        file.close()

    @commands.command(name="g")
    async def generate(self, ctx):
        with open("/Users/me/Documents/Projects/cheemsbot/data.txt") as f:
            text = f.read()
        text_model = markovify.NewlineText(text)
        phrase = text_model.make_sentence()
        while phrase == None:
            phrase = text_model.make_sentence()
        await ctx.send(phrase)


def setup(bot):
    bot.add_cog(GeneratorCog(bot))
