import json

class JSONObject(object):
    def __init__(self, data:str):
        self.__dict__  = json.loads(data)