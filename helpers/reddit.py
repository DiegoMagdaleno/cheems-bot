import praw

class RedditSession():
    def __init__(self, client_id, client_secret, user_agent):
        self.client_id = str(client_id)
        self.client_secret = str(client_secret)
        self.user_agent = str(user_agent)
        self.current_log = praw.Reddit(client_id=self.client_id, client_secret=self.client_secret, user_agent=self.user_agent)

class RedditPost(RedditSession):
    def __init__(self, client_id, client_secret, user_agent, subreddit) -> None:
        self.subreddit = subreddit
        super().__init__(client_id, client_secret, user_agent)
        self.subreddit = subreddit
        self.target = self.current_log.subreddit(self.subreddit).random()

    def get_random_meme(self) -> str:
       return self.target.url

    def get_post_author(self) -> str:
        return str(self.target.author)
    
    def get_post_title(self) -> str:
        return self.target.title
    
    def get_post_subreddit(self) -> str:
        return str(self.target.subreddit)
    
    def get_poster_avatar(self) -> str:
        return str(self.target.author.icon_img)
    
    def get_post_created(self) -> str:
        return reddit_session.subreddit(self.subreddit).random().created_utc
