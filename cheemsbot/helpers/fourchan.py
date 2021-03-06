from dataclasses import dataclass
import random

import basc_py4chan


@dataclass
class FourChanPost:
    submission_url: str
    submission_is_nsfw: bool
    submission_topic: str
    submission_image_url: str
    board_title: str


class FourChan:
    def __init__(self, board: str) -> None:
        self.board = basc_py4chan.Board(board)


class FourChanImage(FourChan):
    def __init__(self, desired_board: str):
        super().__init__(desired_board)

        all_thread_ids = self.board.get_all_thread_ids()
        random_thread = random.choice(all_thread_ids)
        thread = self.board.get_thread(random_thread)

        for f in thread.file_objects():
            self.image_url = f.file_url

        self.topic = str(thread.topic.subject)
        self.url = str(thread.url)
        self.is_nsfw = self.board.is_worksafe
        self.board_title = self.board.title
