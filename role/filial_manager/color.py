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

    @log_decorator
    def add_car_color(self):
        """
        Add a new car color to the database.
        """
        threading.Thread(target=self.create_car_color_table).start()
        color_name = input("Enter car color name: ")
        color_code = input("Enter color code: ")

        query = "INSERT INTO color (NAME, CODE) VALUES (%s, %s)"
        threading.Thread(target=execute_query(query, (color_name, color_code))).start()
        print(f"Car color added successfully with code {color_code}.")
        return None

    @log_decorator
    def show_car_colors(self):
        """
        Show all car colors in the color table.
        """
        query = "SELECT * FROM color;"
        result = execute_query(query, fetch="all")
        print("Car Colors:")
        for color in result:
            print(f"- ID: {color[0]}, Name: {color[1]}, Code: {color[2]}")
        return None
