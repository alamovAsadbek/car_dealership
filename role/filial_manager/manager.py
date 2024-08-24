"""
1. Add new car
2. Update car information
3. Delete car information
4. Show all cars
5. Search car by model
    """
import threading

from main_files.database.db_setting import Database, execute_query
from main_files.decorator.decorator_func import log_decorator


class FilialManager:
    def __init__(self):
        self.db = Database()

    @log_decorator
    def create_car_table(self):
        """
        Create the manager table in the database if it does not already exist.
        """
        query = '''
                CREATE TABLE IF NOT EXISTS filials (
                ID SERIAL PRIMARY KEY,
                NAME VARCHAR(255) NOT NULL,
                ADDRESS VARCHAR(255) NOT NULL,
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
        car_model = input("Enter car model: ")
        car_color = input("Enter car color: ")
        car_year = input("Enter car year: ")

        query = "INSERT INTO cars (NAME, ADDRESS) VALUES (%s, %s)"
        params = (car_model, car_color, car_year)
        threading.Thread(target=execute_query, args=(query, params))
        print("Car added successfully.")
        return None
