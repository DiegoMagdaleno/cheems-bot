# type: ignore

import praw
from dataclasses import dataclass


@dataclass
class RedditCredentials:
    client_id: str
    client_secret: str
    user_agent: str
    user: str
    password: str


class RedditSession:
    def __init__(self, client_id: str, client_secret: str, user_agent: str, user: str, password: str) -> None:
        self.client_id = str(client_id)
        self.client_secret = str(client_secret)
        self.user_agent = str(user_agent)
        self.user = str(user)
        self.password = str(password)
        self.praw_session = praw.Reddit(
            client_id=self.client_id,
            client_secret=self.client_secret,
            user_agent=self.user_agent,
            user=self.user,
            password=self.password,
        )


class RedditPost(RedditSession):
    def __init__(
        self, reddit_credentials: RedditCredentials, subreddit: str
    ) -> None:
        self.reddit_credentials = reddit_credentials
        super().__init__(self.reddit_credentials.client_id, self.reddit_credentials.client_secret,
                         self.reddit_credentials.user_agent, self.reddit_credentials.user, self.reddit_credentials.password)

        # The subreddit we want to targed
        self.subreddit = subreddit

        # We get the subreddit property from our praw session atribute in our main class, and we tell it to get a random post
        self.target = self.praw_session.subreddit(self.subreddit).random()

        self.post_image = self.target.url
        self.post_author = str(self.target.author)
        self.post_title = self.target.title
        self.post_subreddit = str(self.target.subreddit)
        self.post_author_avatar = str(self.target.author.icon_img)
        self.post_link = "https://reddit.com{0}".format(self.target.permalink)
        self.is_nsfw = self.target.over_18
        self.is_only_text = self.target.is_self
