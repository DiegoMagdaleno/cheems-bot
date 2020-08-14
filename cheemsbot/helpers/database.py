import sqlite3

class DataBaseHandlers():
    def __init__(self, connection) -> None:
        self.connection = connection

    def __create_tables(self, conn, instructions):
        self.conn = conn
        self.instructions = instructions
        try:
            c = conn.cursor
            c.execute(self.instructions)
        except sqlite3.Error:
            raise

    def __database_init(self):
        try:
            self.conn = sqlite3.connect(self.connection)
        except sqlite3.Error:
            raise
        finally:
            self.conn.close()
        
        return self.conn
    
    def __init_tables(self):
        self.create_server_configuration_table = """ CREATE TABLE IF NOT EXITS server_configurations (
            guild_id text,
            mute_role text
        ); """
        self.conn = self.__database_init(self.connection)

        if self.conn is not None:
            self.__create_tables(self.create_server_configuration_table)
        else:
            print("Error")
    
    def configure_server(self, conn, configuration):
        self.conn = conn
        self.configuration = configuration
        sql = """ INSERT INTO server_configurations(guild_id, mute_role)
        VALUES (?, ?) """
        self.cursor = self.conn.cursor()
        self.cursor.execute(sql, self.configuration)
        self.conn.commit()
        return self.cursor.lastrowid

