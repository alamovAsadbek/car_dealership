<<<<<<< HEAD
from main_files.decorator.decorator_func import log_decorator
from main_files.database.db_setting import Database

=======
import threading

from main_files.decorator.decorator_func import log_decorator
from main_files.database.db_setting import Database, execute_query
>>>>>>> 7d4a9cd6c48cb800912aea90d5d72f74ea9d5651


class CarsManager:
    def __init__(self):
        self.db = Database()

<<<<<<< HEAD
@log_decorator
def create_quantity_table(self):
=======
    @log_decorator
    def create_quantity_table(self):
>>>>>>> 7d4a9cd6c48cb800912aea90d5d72f74ea9d5651
        """
        Create the quatity table in the database if it does not already exist.
        """
        query = '''
<<<<<<< HEAD
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
=======
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

    @log_decorator
    def add_car_quantity(self):
        """
        Add a new car quantity to the database.
        """
        threading.Thread(target=self.create_quantity_table).start()
        quantity = int(input("Enter car quantity: "))
        model_id = int(input("Enter car model ID: "))
        color_id = int(input("Enter car color ID: "))
        filial_id = int(input("Enter car filial ID: "))
        query = '''
                    INSERT INTO quantity (QUANTITY, MODEL_ID, COLOR_ID, FILIAL_ID)
                    VALUES (%s, %s, %s, %s);
                    '''
        threading.Thread(target=execute_query, args=(query, (quantity, model_id, color_id, filial_id))).start()
        print("Car quantity added successfully.")
        return None
>>>>>>> 7d4a9cd6c48cb800912aea90d5d72f74ea9d5651
