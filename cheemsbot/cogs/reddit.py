import cheemsbot.config as conf
import random
from cheemsbot.helpers import embeds

from discord.errors import NotFound
from discord.ext import commands
from prawcore.exceptions import NotFound


class RedditCommandsCog(commands.Cog, name="Reddit posts and memes"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="dogememe", aliases=["dgmeme"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def dogememe(self, ctx):
        async with ctx.typing():
            self.reddit_post = conf.get_reddit_post("dogelore")
            embed_message = embeds.RedditEmbedMessage(
                self.reddit_post, "meme",
            ).get_embed_message()
        await ctx.send(embed=embed_message)

    @commands.command(name="redditmeme", aliases=["rmeme"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def redditmeme(self, ctx):
        async with ctx.typing():
            self.current_subreddit = random.choice(
                [
                    "me_irl",
                    "okbuddyretard",
                    "okbuddylinux",
                    "surrealmemes",
                    "comedyheaven",
                    "comedynecrophilia",
                    "ComedySeizure",
                    "ComedyCemetery",
                    "DeepFriedMemes",
                ]
            )
            self.reddit_post = conf.get_reddit_post(
                self.current_subreddit, only_image=True
            )
            embed_message = embeds.RedditEmbedMessage(
                self.reddit_post, "meme",
            ).get_embed_message()
        await ctx.send(embed=embed_message)

    @commands.command(name="cringe")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def cringe(self, ctx):
        async with ctx.typing():
            self.current_subreddit = random.choice(
                ["pewdiepiesubmissions", "dankmemes", "meme", "memes", "gaming",]
            )
            self.reddit_post = conf.get_reddit_post(
                self.current_subreddit, only_image=True
            )
            embed_message = embeds.RedditEmbedMessage(
                self.reddit_post, "meme",
            ).get_embed_message()
        await ctx.send(embed=embed_message)

    @commands.command(name="redditpost", aliases=["rpost"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def redditpost(self, ctx, *, subreddit=None):
        self.forbidden = ["cock", "ass", "sex", "dick", "penis", "pussy"]
        self.current_subreddit = subreddit
        if self.current_subreddit is None:
            await ctx.send("Give a subreddit")
            return
        try:
            reddit_post = conf.get_reddit_post(self.current_subreddit)
        except NotFound:
            await ctx.send("Post not found")
            return
        if (reddit_post.is_nsfw) and (ctx.channel.is_nsfw() is False):
            await ctx.send("Not in front of the children.")
            return
        self.string_test_result = any(
            element in self.current_subreddit for element in self.forbidden
        )
        if self.string_test_result and (ctx.channel.is_nsfw() is False):
            await ctx.send(
                "Subreddit contains a forbidden word. This detection will be improved eventually."  # noqa: E501
            )
            return
        embed_message = embeds.RedditEmbedMessage(
            self.reddit_post, "post",
        ).get_embed_message()
        await ctx.send(embed=embed_message)


def setup(bot):
    bot.add_cog(RedditCommandsCog(bot))
