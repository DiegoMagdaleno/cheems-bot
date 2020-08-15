from cheemsbot.helpers import embeds
from discord.ext import commands
import discord
import cheemsbot.config as conf
import random


class RedditCommandsCog(commands.Cog, name="Reddit posts and memes"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="dogememe", aliases=["dgmeme"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def dogememe(self, ctx):
        async with ctx.typing():
            self.reddit_post = conf.get_reddit_post("dogelore")
            embed_message = embeds.RedditEmbedMessage(
                discord.Color.orange(),
                self.reddit_post.post_title,
                self.reddit_post.post_image,
                self.reddit_post.post_subreddit,
                self.reddit_post.post_author,
                self.reddit_post.post_author_avatar,
                self.reddit_post.post_link,
                "meme"
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
                ]
            )
            self.reddit_post = conf.get_reddit_post(self.current_subreddit, only_image=True)
            embed_message = embeds.RedditEmbedMessage(
                discord.Color.orange(),
                self.reddit_post.post_title,
                self.reddit_post.post_image,
                self.reddit_post.post_subreddit,
                self.reddit_post.post_author,
                self.reddit_post.post_author_avatar,
                self.reddit_post.post_link,
                "meme",
            ).get_embed_message()
        await ctx.send(embed=embed_message)

    @commands.command(name="cringe")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def cringe(self, ctx):
        async with ctx.typing():
            self.current_subreddit = random.choice(
                [
                    "pewdiepiesubmissions",
                    "dankmemes",
                    "meme",
                    "memes",
                    "gaming",
                ]
            )
            self.reddit_post = conf.get_reddit_post(self.current_subreddit, only_image=True)
            embed_message = embeds.RedditEmbedMessage(
                discord.Color.orange(),
                self.reddit_post.post_title,
                self.reddit_post.post_image,
                self.reddit_post.post_subreddit,
                self.reddit_post.post_author,
                self.reddit_post.post_author_avatar,
                self.reddit_post.post_link,
                "meme",
            ).get_embed_message()
        await ctx.send(embed=embed_message)

    @commands.command(name="redditpost", aliases=["rpost"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def redditpost(self, ctx, *, subreddit=None):
        self.forbidden = ["cock", "ass", "sex", "dick", "penis", "pussy"]
        self.current_subreddit = subreddit
        if self.current_subreddit is None:
            await ctx.send("Give a subreddit")
        else:
            reddit_post = conf.get_reddit_post(self.current_subreddit)
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
                discord.Color.orange(),
                reddit_post.post_title,
                reddit_post.post_image,
                reddit_post.post_subreddit,
                reddit_post.post_author,
                reddit_post.post_author_avatar,
                reddit_post.post_link,
                "post",
            ).get_embed_message()
            await ctx.send(embed=embed_message)


def setup(bot):
    bot.add_cog(RedditCommandsCog(bot))
