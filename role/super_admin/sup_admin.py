from main_files.database.db_setting import Database
from main_files.decorator.decorator_func import log_decorator


class Super_admin:
    def __init__(self):
        self.__database = None
        self.db = Database

    @log_decorator
    def create_filial_table(self):
        """
               Create the users table in the database if it does not already exist.
        """
        query = '''
            CREATE TABLE IF NOT EXISTS filials (
            ID SERIAL PRIMARY KEY,
            NAME VARCHAR(255) NOT NULL,
            ADDRESS VARCHAR(255) NOT NULL,
            CREATED_AT TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
            );
            '''
        with self.__database as cursor:
            cursor.execute(query)
        return True
