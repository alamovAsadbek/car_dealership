import threading

from main_files.database.db_setting import Database, execute_query
from main_files.decorator.decorator_func import log_decorator


class ColorManager:
    def __init__(self):
        self.db = Database()

    @log_decorator
    def create_car_color_table(self):
        """
        Create the manager table in the database if it does not already exist.
        """
        query = '''
                    CREATE TABLE IF NOT EXISTS color (
                    ID SERIAL PRIMARY KEY,
                    NAME VARCHAR(255) NOT NULL,
                    CODE VARCHAR(255) NOT NULL UNIQUE
                    );
                '''
        with self.db as cursor:
            cursor.execute(query)
            return None


