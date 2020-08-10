from os import O_RANDOM
from re import sub
import praw
from praw.models import user
from praw.models.listing.mixins import subreddit
from .config import Configuration

reddit_session_credentials = Configuration()

reddit_session = praw.Reddit(client_id=str(reddit_session_credentials.get_reddit_client_id()),
                             client_secret=str(reddit_session_credentials.get_client_secret()),
                             user_agent=str(reddit_session_credentials.get_user_agent()))

class RedditPost():
    def __init__(self, subreddit) -> None:
        self.subreddit = subreddit
    
    def get_random_meme(self) -> str:
       return reddit_session.subreddit(self.subreddit).random().url

    
    def get_post_author(self) -> str:
        return str(reddit_session.subreddit(self.subreddit).random().author)
    
    def get_post_title(self) -> str:
        return reddit_session.subreddit(self.subreddit).random().title
    
    def get_post_subreddit(self) -> str:
        return str(reddit_session.subreddit(self.subreddit).random().subreddit)
    
    def get_poster_avatar(self) -> str:
        return str(reddit_session.subreddit(self.subreddit).random().author.icon_img)
    
    def get_post_created(self) -> str:
        return reddit_session.subreddit(self.subreddit).random().created_utc



def get_reddit_meme() -> str:
    doge_lore_session = reddit_session.subreddit('dogelore').random()
    return doge_lore_session.url
