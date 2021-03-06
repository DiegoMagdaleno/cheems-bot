from cheemsbot.helpers import embeds
import cheemsbot.config as conf
import random
from cheemsbot.helpers import nekoimg
from cheemsbot.helpers import random_operations
from cheemsbot.helpers import fourchan
from cheemsbot.helpers import stringchecker
from cheemsbot.helpers import poll
from disputils import BotMultipleChoice
from cheemsbot.helpers import errorhandler

import discord
from discord.ext import commands
from lmgtfyreborn.main import Lmgtfy
import requests


class FunWithCheemsCog(commands.Cog, name="Fun"):
    """A set of misc actions, that allow users to perform some fun operations."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ask", aliases=["8b"])
    async def ask(self, ctx, *, question=None):
        """Description: Gives an answer to a question asked by a user. Similar to 8ball.\nArguments: `1`"""
        if question is None:
            await ctx.send(
                embed=errorhandler.BotAlert("warn", "You need to ask something"
                ).get_error_embed()
            )
        else:
            ask_answer = random_operations.get_8_ball()
            await ctx.send(f"{ctx.author.mention}, {ask_answer}")

    @commands.command(name="gf")
    async def girlfriend(self, ctx):
        """Description: Grabs an image from r/gentlemanboners, and displays it \nArguments: `None`"""
        self.reddit_post = conf.get_reddit_post("gentlemanboners")
        await ctx.send(self.reddit_post.image)

    @commands.command(name="bf")
    async def boyfriend(self, ctx):
        """Description: Grabs an image from r/ladybonners, and displays it \nArguments: `None`"""
        self.reddit_post = conf.get_reddit_post("ladyboners")
        await ctx.send(self.reddit_post.image)

    @commands.command(name="femboy")
    async def femboy(self, ctx):
        """Description: Grabs an image from r/femboy, and displays it \nArguments: `None`"""
        reddit_post = conf.get_reddit_post("femboy")
        await ctx.send(reddit_post.image)

    @commands.command(name="neko")
    async def neko(self, ctx):
        """Description: Grabs an image from nekos.life and displays it.\nArguments: `None`"""
        self.neko_img = nekoimg.get_neko_sfw()
        await ctx.send(self.neko_img)

    @commands.command(name="owofy")
    async def owofy(self, ctx, *, our_input=None):
        """Description: Owofies sewected input UwU\nArguments: `1`"""
        if our_input is None:
            await ctx.send(
                embed=errorhandler.BotAlert("warn", "You need to give a message to owofy"
                ).get_error_embed()
            )
            return
        self.string_check_session = stringchecker.StringChecker(our_input)
        if self.string_check_session.is_unicode() is False:
            await ctx.send(
                embed=errorhandler.BotAlert("warn", "Nice try on bypassing. However Cheems doesn't accept unicode."
                ).get_error_embed()
            )
            return
        if self.string_check_session.contains_racism():
            await ctx.send(
                embed=errorhandler.BotAlert("warn", "Cheems does not repeat or talks to racists."
                ).get_error_embed()
            )
            return
        self.owofied_input = nekoimg.owo_text(our_input)
        await ctx.send(self.owofied_input)

    @commands.command(name="ischad")
    async def ischad(self, ctx, member: discord.User = None):
        """Description: Tells you if an user is a Chad or a Beta based on luck.\nArguments: `1`"""
        self.current_member = member
        if self.current_member is None:
            await ctx.send(
                embed=errorhandler.BotAlert("warn", "You need to provide an user."
                ).get_error_embed()
            )
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

    @commands.command(name="lmgtfy")
    async def lmgtfy(self, ctx, *, our_terms=None):
        """Description: Generates an URL to lmgtfy containing your desired search terms\nArguments: `1`"""
        if our_terms is None:
            await ctx.send(
                errorhandler.BotAlert("warn", "You need to provide a query."
                ).get_error_embed()
            )
        else:
            self.lmgtfy_list = our_terms.split()
            await ctx.send(Lmgtfy(self.lmgtfy_list).get_url())

    @commands.command(name="animegf")
    async def animegf(self, ctx):
        """Description: Grabs an image from 4chan's /c/ board and displays it \nArguments: `None`"""
        self.fourchan_image = fourchan.FourChanImage("c").image_url
        await ctx.send(self.fourchan_image)

    @commands.command(name="animebf")
    async def animebf(self, ctx):
        """Description: Grabs an image from 4chan's /cm/ board and displays it \nArguments: `None`"""
        self.fourchan_image = fourchan.FourChanImage("cm").image_url
        await ctx.send(self.fourchan_image)

    # TODO: Right now we can't do our self.target.clone = ctx.author because of Python limitations
    # however with python 3.10 we will be able to do membed: discord.user | str
    # or no :p
    @commands.command(name="clone")
    async def clone(self, ctx, member: discord.User = None, *, message=None):
        """Description: Replicates what an user says, if no user is provided it will clone the message author\nArguments: `1 up to 2`"""
        if member is None and message is None:
            await ctx.send(
                embed=errorhandler.BotAlert("warn", "You need to provide an user and a message."
                ).get_error_embed()
            )
            return
        if "@" in message or "<" in message or "&" in message:
            await ctx.send(
                embed=errorhandler.BotAlert("warn", "I will not ping another user/a role/or everyone"
                ).get_error_embed()
            )
            return
        self.target_to_clone = member
        self.profile_picture = requests.get(
            self.target_to_clone.avatar_url_as(format="png", size=256)
        ).content
        self.hook = await ctx.channel.create_webhook(
            name=self.target_to_clone.display_name, avatar=self.profile_picture
        )

        await self.hook.send(message)
        await self.hook.delete()

    @commands.command(name="poll")
    async def poll(self, ctx, *, desired_questions: str = None):
        if desired_questions is None:
            await ctx.send(
                embed=errorhandler.BotAlert("warn",
                    "What do you want a poll about? Syntax: Question, options, separated, by, commas",
                )
            )
            return
        self.split_questions = desired_questions.split(",")
        self.question = self.split_questions[0]
        self.split_questions.pop(0)
        try:
            self.poll_verify = poll.PollHelper(self.split_questions).verify_poll()
        except poll.PollException:
            await ctx.send(
                embed=errorhandler.BotAlert("error", "Limit exeded").get_error_embed()
            )
            return
        self.multiple_choice = BotMultipleChoice(
            ctx, self.split_questions, self.question
        )
        await self.multiple_choice.run()


def setup(bot):
    bot.add_cog(FunWithCheemsCog(bot))
