# type: ignore

import praw


class RedditSession():
    def __init__(self, client_id, client_secret, user_agent, user, password):
        self.client_id = str(client_id)
        self.client_secret = str(client_secret)
        self.user_agent = str(user_agent)
        self.user = str(user)
        self.password = str(password)
        self.current_log = praw.Reddit(
            client_id=self.client_id, client_secret=self.client_secret, user_agent=self.user_agent, user=self.user, password=self.password)


class RedditPost(RedditSession):
    def __init__(self, client_id, client_secret, user_agent, user, password, subreddit) -> None:
        self.subreddit = subreddit
        super().__init__(client_id, client_secret, user_agent, user, password)
        self.subreddit = subreddit
        self.target = self.current_log.subreddit(self.subreddit).random()
        self.post_image = self.target.url
        self.post_author = str(self.target.author)
        self.post_title = self.target.title
        self.post_subreddit = str(self.target.subreddit)
        self.post_author_avatar = str(self.target.author.icon_img)
        self.post_link = "https://reddit.com" + self.target.permalink
        self.is_nsfw = self.target.over_18
        self.is_only_text = self.target.is_self