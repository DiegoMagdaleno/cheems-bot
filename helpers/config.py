import os
import json
from os import sendfile
from .misc import JSONObject
from typing import *
class Configuration:

    def __init__(self, json_file) -> None:
        load_json = str(json.loads(json_file)).replace('\'', '"')
        self.config_session = JSONObject(load_json)

    def get_reddit_client_id(self) -> str:
        return self.config_session.redditClientID

    def get_client_secret(self) -> str:
        return self.config_session.redditClientSecret

    def get_user_agent(self) -> str:
        return self.config_session.redditUserAgent
