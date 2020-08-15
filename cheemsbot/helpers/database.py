# Project Kanji Automcompiler Database handler

import sqlite3


class DatabaseHandler:
    def __init__(self, db_name, default_table=1):
        self.db_name = db_name
        self.db = sqlite3.connect(db_name)
        self.default_table = default_table

    def add_server(self, server_name):

        self.columns = {
            "mute_role": "text",
        }

        self.db.execute(
            "CREATE TABLE IF NOT EXISTS {}({})".format(server_name, self.columns)
        )
