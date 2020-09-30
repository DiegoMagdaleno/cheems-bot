from typing import List


class PollException(Exception):
    pass


class PollHelper:
    def __init__(self, items: List):
        self.items = items

    def verify_poll(self):
        if len(self.items) > 10:
            raise PollException
