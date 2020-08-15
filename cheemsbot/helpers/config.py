import json
from cheemsbot.helpers.misc import JSONObject


class Configuration:
    def __init__(self, json_file: str) -> None:
        load_json = str(json.loads(json_file)).replace("'", '"')
        self.config_session = JSONObject(load_json)
        self.reddit_client_id = self.config_session.redditClientID
        self.reddit_client_secret = self.config_session.redditClientSecret
        self.reddit_user_agent = self.config_session.redditUserAgent
        self.reddit_user = self.config_session.redditUser
        self.reddit_password = self.config_session.redditPassword
        self.discord_token = self.config_session.discordToken
