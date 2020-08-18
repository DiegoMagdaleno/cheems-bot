import cheemsbot.config as conf
import random
from cheemsbot.helpers import embeds

from discord.errors import NotFound
from discord.ext import commands
from prawcore.exceptions import Forbidden, NotFound


class RedditCommandsCog(commands.Cog, name="RedditActions"):
    """A set of actions to get contents from Reddit displayed!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="dogememe", aliases=["dgmeme"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def dogememe(self, ctx):
        """Description:  Grabs a random meme from r/Dogelore and posts it in chat\nArguments: `None`"""
        async with ctx.typing():
            self.reddit_post = conf.get_reddit_post("dogelore")
            embed_message = embeds.RedditEmbedMessage(
                self.reddit_post, "meme",
            ).get_embed_message()
        await ctx.send(embed=embed_message)

    @commands.command(name="redditmeme", aliases=["rmeme"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def redditmeme(self, ctx):
        """Description:  Grabs an image from the following subreddits:\n •me_irl\n   •okbuddyret*rd\n    •okbuddylinux\n •surrealmemes\n  •comedyheaven\n    •comedynecrophilia\n    •comedyseizure\n    •comedycementery\n•DeepFriendMemes \nand posts it in the chat.\nArguments: `None`"""
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
        """Description:  Grabs an image from the following Subreddits:\n •PewDiePieSubmissions\n   •Dankmemes\n    •memes\n •meme\n •gamging \nand posts it in chat\nArguments: `None`"""
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
        """Description: Grabs a post from a desired subreddit, provided by the user, if the post is NSFW it will only display on NSFw channels\nArguments: `1`"""
        self.forbidden = ["cock", "ass", "sex", "dick", "penis", "pussy"]
        self.current_subreddit = subreddit
        if self.current_subreddit is None:
            await ctx.send("Give a subreddit")
            return
        async with ctx.typing():
            try:
                self.reddit_post = conf.get_reddit_post(self.current_subreddit)
            except NotFound:
                await ctx.send("Subreddit not found")
                return
            except Forbidden:
                await ctx.send(
                    "I don't have permissions to watch that subreddit. Perhaps it is quarantined."
                )
                return
            if (self.reddit_post.is_nsfw) and (ctx.channel.is_nsfw() is False):
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
