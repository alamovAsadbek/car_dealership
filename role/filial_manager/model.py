import threading

from main_files.database.db_setting import execute_query, Database
from main_files.decorator.decorator_func import log_decorator


class ModelManager:
    def __init__(self):
        self.db = Database()

    def create_model_table(self):
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
    def add_car_model(self):
        """
        Add a new car brand to the database.
        """
        threading.Thread(target=self.create_brand_table).start()
        brand_name = input("Enter car brand name: ")

        query = "INSERT INTO brand (NAME) VALUES (%s)"
        threading.Thread(target=execute_query(query, (brand_name,))).start()
        print(f"Car brand added successfully.")
        return None

    @log_decorator
    def show_all_model(self):
        """
        Show all car brands in the brand table.
        """
        query = "SELECT * FROM brand;"
        result = execute_query(query, fetch="all")
        print("Car Brands:")
        for brand in result:
            print(f"- ID: {brand[0]}, Name: {brand[1]}")
        return None
