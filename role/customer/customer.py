import threading

from main_files.database.db_setting import Database, execute_query
from main_files.decorator.decorator_func import log_decorator
from psycopg2 import sql


class CostumerManager:
    def __init__(self):
        self.db = Database()

