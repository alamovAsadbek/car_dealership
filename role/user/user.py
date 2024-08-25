import hashlib
from main_files.database.db_setting import Database, execute_query
from main_files.decorator.decorator_func import log_decorator

class UserManager:
    def __init__(self):
        self.db = Database()
