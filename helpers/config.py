import os
import json
from os import sendfile
from .misc import JSONObject
from typing import *

path = os.path.abspath("config.json")

fileLoad = open(path, 'r').read()
stored_json_load = str(json.loads(fileLoad)).replace('\'', '"')
config_session = JSONObject(stored_json_load)


class Configuration:

    def get_reddit_client_id(self) -> str:
        return config_session.redditClientID

    def get_client_secret(self) -> str:
        return config_session.redditClientSecret

    def get_user_agent(self) -> str:
        return config_session.redditUserAgent
