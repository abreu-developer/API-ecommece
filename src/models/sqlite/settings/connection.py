import sqlite3
from sqlite3 import Connection

class SqliteConnectHandler:
    def __init__(self):
        self.__connection_string = "storage.db"
        self.__conn = None

    def connect(self) -> Connection:
        conn = sqlite3.connect(
            self.__connection_string,
            check_same_thread=False
            )

        self.__conn = conn
        return conn

    def get_connection(self) -> Connection:
        return self.__conn
