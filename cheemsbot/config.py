import os
from typing import List

from cheemsbot.helpers import config
from cheemsbot.helpers import reddit
from cheemsbot.helpers import ghelper

config_path = os.path.abspath("config.json")
file_load = open(config_path, "r").read()
session_config = config.Configuration(file_load)

our_reddit_credentials = reddit.RedditCredentials(
    session_config.reddit_client_id,
    session_config.reddit_client_secret,
    session_config.reddit_user_agent,
    session_config.reddit_user,
    session_config.reddit_password,
)


our_discord_token = session_config.discord_token

our_google_credentials = ghelper.GoogleCredentials(
    session_config.google_api_key, session_config.google_cx
)


def get_reddit_post(
    subreddit: str, only_image: bool = False
) -> reddit.RedditPostContents:
    reddit_post = reddit.RedditPost(our_reddit_credentials, subreddit)

    # ! NOTICE: This method significaly slow downs our bot (about 30%) but its
    # ! our only solution, until support for Reddit galleries is added.
    # ! Note that Reddit will never be perfect, as we don't have a way to be 100%
    # ! What we grabbed is an image, still it is recommended for maintainers
    # ! And contributors of this project to keep an eye on Praw documentation and this
    # ! issue: https://github.com/praw-dev/praw/issues/1549
    if only_image:
        while reddit_post.is_only_text and "i.redd.it" not in reddit_post.image:
            reddit_post = reddit.RedditPost(our_reddit_credentials, subreddit)
    reddit_contents = reddit.RedditPostContents(
        reddit_post.title,
        reddit_post.image,
        reddit_post.subreddit,
        reddit_post.author,
        reddit_post.author_avatar,
        reddit_post.link,
        reddit_post.is_nsfw,
    )
    return reddit_contents


def get_images(term: str, safe_search: str) -> List:
    list_of_images = ghelper.GoogleImageSearch(
        google_credentials=our_google_credentials,
        search_term=term,
        safe_search=safe_search,
    ).link_list
    return list_of_images
