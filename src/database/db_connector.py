"""
    Module for creating database connection whenever we need to perform any database operations.
    DatabaseConnection class is implemented following Singleton Design pattern.
"""
import sqlite3
from sqlite3 import Connection

class DatabaseConnection:
    """
        Class for creating and closing database connection.
    """
    def __init__(self, host) -> None:
        self.connection = None
        self.host = host

    def __enter__(self) -> Connection:
        self.connection = sqlite3.connect(self.host)
        return self.connection
   
    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        if exc_type or exc_val or exc_tb:
            print(exc_type, exc_val)
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()