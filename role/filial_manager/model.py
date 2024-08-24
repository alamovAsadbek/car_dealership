import threading

from main_files.database.db_setting import execute_query
from main_files.decorator.decorator_func import log_decorator


def create_brand_table(self):
    """
    Create the car brand table in the database if it does not already exist.
    """
    query = '''
            CREATE TABLE IF NOT EXISTS brand (
            ID SERIAL PRIMARY KEY,
            NAME VARCHAR(255) NOT NULL,
            );
        '''
    with self.db as cursor:
        cursor.execute(query)
        return None

