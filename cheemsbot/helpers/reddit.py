# type: ignore
import random
from dataclasses import dataclass

import praw


@dataclass
class RedditCredentials:
    client_id: str
    client_secret: str
    user_agent: str
    user: str
    password: str


@dataclass
class RedditPostContents:
    title: str
    image: str
    subreddit: str
    author: str
    author_avatar: str
    link: str
    is_nsfw: bool


class RedditSession:
    def __init__(
        self,
        client_id: str,
        client_secret: str,
        user_agent: str,
        user: str,
        password: str,
    ) -> None:
        self.client_id: str = str(client_id)
        self.client_secret: str = str(client_secret)
        self.user_agent: str = str(user_agent)
        self.user: str = str(user)
        self.password: str = str(password)
        self.praw_session: praw.Reddit = praw.Reddit(
            client_id=self.client_id,
            client_secret=self.client_secret,
            user_agent=self.user_agent,
            user=self.user,
            password=self.password,
        )


class RedditPost(RedditSession):
    def __init__(self, reddit_credentials: RedditCredentials, subreddit: str) -> None:
        self.reddit_credentials = reddit_credentials
        super().__init__(
            self.reddit_credentials.client_id,
            self.reddit_credentials.client_secret,
            self.reddit_credentials.user_agent,
            self.reddit_credentials.user,
            self.reddit_credentials.password,
        )

        # The subreddit we want to targed
        self.subreddit = subreddit

        # We get the subreddit property from our praw session attribute in our main class,
        # and we tell it to get a random post
        self.target = self.praw_session.subreddit(self.subreddit).random()

        # Some subreddits don't support the random feature, so we do it ourselves.
        if self.target is None:
            self.random_id_choice = random.choice(
                list(self.praw_session.subreddit(self.subreddit).hot(limit=50))
            )
            self.target = self.praw_session.submission(self.random_id_choice)

        self.image = self.target.url
        self.author = str(self.target.author)
        self.title = self.target.title
        self.subreddit = str(self.target.subreddit)
        self.author_avatar = str(self.target.author.icon_img)
        self.link = "https://reddit.com{0}".format(self.target.permalink)
        self.is_nsfw = self.target.over_18
        self.is_only_text = self.target.is_self
