from cheemsbot.helpers.reddit import RedditPost
import os
from cheemsbot.helpers import config, reddit

config_path = os.path.abspath("config.json")
file_load = open(config_path, "r").read()
session_config = config.Configuration(file_load)

our_reddit_credentials = reddit.RedditCredentials(session_config.reddit_client_id, session_config.reddit_client_secret,
                                                  session_config.reddit_user_agent, session_config.reddit_user, session_config.reddit_password)


our_discord_token = session_config.discord_token

def get_reddit_post(subreddit:str) ->  RedditPost:
    reddit_post = reddit.RedditPost(
        our_reddit_credentials,
        subreddit
    )
    return reddit_post
