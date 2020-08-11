import discord
from discord.ext import commands
from helpers import config, reddit, embeds, random_operations, fourchan, nekoimg
import os
import sys
import traceback


bot = commands.Bot(command_prefix='>')
config_path = os.path.abspath("config.json")
file_load = open(config_path, 'r').read()

session_config = config.Configuration(file_load)

initial_extensions = ['cogs.fun', 'cogs.nekoactions']
if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()


@bot.command()
async def ping(ctx):
    random_cheems = random_operations.get_cheems_phrase()
    await ctx.send(random_cheems)


@bot.command()
async def dogememe(ctx):
    reddit_post = reddit.RedditPost(session_config.reddit_client_id,
                                    session_config.reddit_client_secret, session_config.reddit_user_agent, session_config.reddit_user, session_config.reddit_password, "dogelore")
    embed_message = embeds.RedditEmbedMessage(discord.Color.orange(), reddit_post.post_title, reddit_post.post_image,
                                              reddit_post.post_subreddit, reddit_post.post_author, reddit_post.post_author_avatar, reddit_post.post_link).getEmbedMessage()
    await ctx.send(embed=embed_message)

@bot.command()
async def tech(ctx):
    target_board = 'g'
    fourchan_post = fourchan.FourChanImage(target_board)
    embed_message = embeds.FourChanEmbed(discord.Color.green(
    ), fourchan_post.topic, fourchan_post.image_url, target_board, fourchan_post.url).getEmbedMessage()
    await ctx.send(embed=embed_message)


@bot.command()
async def lewdfemboy(ctx):
    if ctx.channel.is_nsfw():
        reddit_post = reddit.RedditPost(session_config.reddit_client_id,
                                        session_config.reddit_client_secret, session_config.reddit_user_agent, session_config.reddit_user, session_config.reddit_password,
                                        "femboys")
        await ctx.send(reddit_post.post_image)
    else:
        await ctx.send('Not infromt of the childmren.')


@bot.command()
async def lewdneko(ctx):
    if ctx.channel.is_nsfw():
        await ctx.send(nekoimg.get_neko_nsfw())
    else:
        await ctx.send("Not infromt of the childmren.")


@bot.command()
async def redditmeme(ctx, *, subreddit=None):
    if subreddit == None:
        await ctx.send("Gimve me a sumbreddit")
    else:
        reddit_post = reddit.RedditPost(session_config.reddit_client_id,
                                        session_config.reddit_client_secret, session_config.reddit_user_agent, session_config.reddit_user, session_config.reddit_password,
                                        subreddit)
        if reddit_post.is_nsfw:
            await ctx.send("Not infromt of the childdrem")
            return
        embed_message = embeds.RedditEmbedMessage(discord.Color.orange(), reddit_post.post_title, reddit_post.post_image,
                                                  reddit_post.post_subreddit, reddit_post.post_author, reddit_post.post_author_avatar, reddit_post.post_link).getEmbedMessage()
        await ctx.send(embed=embed_message)

bot.run(session_config.discord_token)
