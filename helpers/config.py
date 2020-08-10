import json
from .misc import JSONObject
from typing import *


class Configuration:

    def __init__(self, json_file) -> None:
        load_json = str(json.loads(json_file)).replace('\'', '"')
        self.config_session = JSONObject(load_json)
        self.reddit_client_id = self.config_session.redditClientID
        self.reddit_client_secret = self.config_session.redditClientSecret
        self.reddit_user_agent = self.config_session.redditUserAgent
        self.discord_token = self.config_session.discordToken
