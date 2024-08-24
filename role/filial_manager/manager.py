import threading
import uuid

from main_files.database.db_setting import Database, execute_query
from main_files.decorator.decorator_func import log_decorator


def generate_color_code():
    """
    Generate a unique UUID for color code.
    """
    return str(uuid.uuid4())


class FilialManager:
    def __init__(self):
        self.db = Database()

    @log_decorator
    def create_car_table(self):
        """
        Create the car table in the database if it does not already exist.
        """
        query = '''
                CREATE TABLE IF NOT EXISTS car (
                ID SERIAL PRIMARY KEY,
                NAME VARCHAR(255) NOT NULL,  
                BRAND_ID BIGINT NOT NULL REFERENCES brand(ID),
                MODEL VARCHAR(255) NOT NULL,
                YEAR INT NOT NULL,
                COLOR_ID BIGINT NOT NULL REFERENCES color(ID),
                FILIAL_ID BIGINT NOT NULL REFERENCES filial(ID),
                CREATED_AT TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
                );
            '''
        with self.db as cursor:
            cursor.execute(query)
            return None
