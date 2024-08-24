import threading

from main_files.database.db_setting import Database, execute_query
from main_files.decorator.decorator_func import log_decorator


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
                YEAR INT NOT NULL,
                MODEL_ID BIGINT NOT NULL REFERENCES MODEL(ID),
                COLOR_ID BIGINT NOT NULL REFERENCES color(ID),
                BRAND_ID BIGINT NOT NULL REFERENCES brand(ID),
                FILIAL_ID BIGINT NOT NULL REFERENCES filial(ID),
                CREATED_AT TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
                );
            '''
        with self.db as cursor:
            cursor.execute(query)
            return None

    @log_decorator
    def add_car(self):
        """
        Add a new car to the database.
        """
        threading.Thread(target=self.create_car_table).start()
        car_name = input("Enter car name: ")
        brand_id = int(input("Enter car brand ID: "))
        model = input("Enter car model: ")
        year = int(input("Enter car year: "))
        color_id = int(input("Enter car color ID: "))
        filial_id = int(input("Enter car filial ID: "))

        query = '''
                INSERT INTO car (NAME, BRAND_ID, MODEL, YEAR, COLOR_ID, FILIAL_ID) 
                VALUES (%s, %s, %s, %s, %s, %s);
            '''
        threading.Thread(target=execute_query,
                         args=(query, (car_name, brand_id, model, year, color_id, filial_id))).start()
        print("Car added successfully.")
        return None

