from dataclasses import dataclass
from loguru import logger as log

import udpy

class UrbanDictionaryError(Exception):
    pass

@dataclass
class UrbanDictionaryEntry:
    word: str
    definition: str
    example: str
    upvotes: int
    downvotes: int

class UrbanDictionary:
    def __init__(self, term) -> None:
        self.term = term
        self.client = UrbanClient() # init UrbanClient
        self.urban_request = self.client.get_definition(self.term)