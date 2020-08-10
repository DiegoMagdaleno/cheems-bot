import random
import basc_py4chan


class FourChan():
    def __init__(self, board) -> None:
        self.board = basc_py4chan.Board(board)

class FourChanImage(FourChan):
    def __init__(self, desired_board):
        super().__init__(desired_board)

        all_thread_ids = self.board.get_all_thread_ids()
        random_thread = random.choice(all_thread_ids)
        thread = self.board.get_thread(random_thread)

        for f in thread.file_objects():
            self.image_url = f.file_url


