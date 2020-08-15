from discord.ext import commands
from cheemsbot.helpers import nekoimg, random_operations
import random
import discord
import cheemsbot.config as conf


class FunWithCheemsCog(commands.Cog, name="Fun with cheemsburger"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ask", aliases=["8b"])
    async def ask(self, ctx, *, question=None):
        if question == None:
            await ctx.send("I meed you to amsk somethimg")
        else:
            ask_answer = random_operations.get_8_ball()
            await ctx.send("{0}, {1}".format(ctx.author.mention, ask_answer))

    @commands.command(name="gf")
    async def girlfriend(self, ctx):
        self.reddit_post = conf.get_reddit_post("gentlemanboners")
        await ctx.send(self.reddit_post.post_image)

    @commands.command(name="bf")
    async def boyfriend(self, ctx):
        self.reddit_post = conf.get_reddit_post("ladyboners")
        await ctx.send(self.reddit_post.post_image)

    @commands.command(name="femboy")
    async def femboy(self, ctx):
        reddit_post = conf.get_reddit_post("femboy")
        await ctx.send(reddit_post.post_image)

    @commands.command(name="neko")
    async def neko(self, ctx):
        self.neko_img = nekoimg.get_neko_sfw()
        await ctx.send(self.neko_img)

    @commands.command(name="owofy")
    async def owofy(self, ctx, *, our_input=None):
        if our_input == None:
            await ctx.send("Gimve me a memsage")
        else:
            self.owofied_input = nekoimg.owo_text(our_input)
            await ctx.send(self.owofied_input)

    @commands.command(name="ischad")
    async def ischad(self, ctx, member: discord.User = None):
        self.current_member = member
        if self.current_member == None:
            await ctx.send("Gimve me a user")
        else:
            self.chad_virgin_prob = random.randint(0, 100)
            if self.chad_virgin_prob >= 50:
                await ctx.send(
                    f"{member.mention} is a chad! <:chad:741875439940665365>"
                )
            else:
                await ctx.send(
                    f"{member.mention} is a beta! <:virgin:741907301627199499>"
                )


def setup(bot):
    bot.add_cog(FunWithCheemsCog(bot))
