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

    @log_decorator
    def create_car_color_table(self):
        """
        Create the manager table in the database if it does not already exist.
        """
        query = '''
                CREATE TABLE IF NOT EXISTS color (
                ID SERIAL PRIMARY KEY,
                NAME VARCHAR(255) NOT NULL,
                CODE VARCHAR(255) NOT NULL
                );
            '''
        with self.db as cursor:
            cursor.execute(query)
            return None

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

    @log_decorator
    def add_car_color(self):
        """
        Add a new car color to the database.
        """
        threading.Thread(target=self.create_car_color_table).start()
        color_name = input("Enter car color name: ")
        color_code = generate_color_code()

        query = "INSERT INTO color (NAME, CODE) VALUES (%s, %s)"
        threading.Thread(target=execute_query(query, (color_name, color_code)))
        print(f"Car color added successfully with code {color_code}.")
        return None

    @log_decorator
    def add_car_brand(self):
        """
        Add a new car brand to the database.
        """
        threading.Thread(target=self.create_brand_table).start()
        brand_name = input("Enter car brand name: ")

        query = "INSERT INTO brand (NAME) VALUES (%s)"
        threading.Thread(target=execute_query(query, (brand_name,)))
        print(f"Car brand added successfully.")
        return None