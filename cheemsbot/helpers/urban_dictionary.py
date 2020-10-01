from loguru import logger as log

import udpy


class UrbanDictionaryError(Exception):
    pass


class UrbanDictionary:
    def __init__(self, term) -> None:
        self.term = term
        self.client = udpy.UrbanClient()

    def get_urban_definitions(self):
        self.urban_request = self.client.get_definition(self.term)
        if len(self.urban_request) == 0:
            raise UrbanDictionaryError
        return self.urban_request
