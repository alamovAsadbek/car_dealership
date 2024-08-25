from main_files.decorator.decorator_func import log_decorator
from main_files.database.db_setting import Database



class CarsManager:
    def __init__(self):
        self.db = Database()

@log_decorator
def create_quantity_table(self):
        """
        Create the quatity table in the database if it does not already exist.
        """
        query = '''
                CREATE TABLE IF NOT EXISTS quantity (
                ID SERIAL PRIMARY KEY,
                QUANTITY BIGINT NOT NULL,
                MODEL_ID BIGINT NOT NULL REFERENCES MODEL(ID),
                COLOR_ID BIGINT NOT NULL REFERENCES color(ID),
                FILIAL_ID BIGINT NOT NULL REFERENCES filial(ID),
                );
            '''
        with self.db as cursor:
            cursor.execute(query)
            return None