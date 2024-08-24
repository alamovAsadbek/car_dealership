import threading

from main_files.database.db_setting import Database, execute_query
from main_files.decorator.decorator_func import log_decorator


class CarsManager:
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

    @log_decorator
    def update_car(self):
        """
        Update the details of a car in the database.
        """
        car_id = int(input("Enter car ID: "))
        car_name = input("Enter new car name: ")
        brand_id = int(input("Enter new car brand ID: "))
        model = input("Enter new car model id: ")
        year = int(input("Enter new car year: "))
        color_id = int(input("Enter new car color ID: "))
        filial_id = int(input("Enter new car filial ID: "))
        query = '''
                UPDATE car 
                SET NAME=%s, BRAND_ID=%s, MODEL=%s, YEAR=%s, COLOR_ID=%s, FILIAL_ID=%s 
                WHERE ID=%s;
            '''
        params = (car_name, brand_id, model, year, color_id, filial_id, car_id)
        threading.Thread(target=execute_query, args=(query, params)).start()
        print("Car details updated successfully.")
        return None

    @log_decorator
    def delete_car(self):
        """
        Delete a car from the database.
        """
        car_id = int(input("Enter car ID: "))
        query = "DELETE FROM car WHERE ID=%s"
        threading.Thread(target=execute_query, args=(query, (car_id,))).start()
        print(f"Car ID {car_id} deleted successfully.")
        return None

    @log_decorator
    def search_car(self):
        """
        Search for cars by name in the car table.
        """
        name = input("Car Name: ")
        query = "SELECT * FROM car WHERE NAME LIKE %s;"
        result = execute_query(query, params=("%" + name + "%",), fetch="all")
        print("Cars:")
        for car in result:
            print(
                f"- ID: {car[0]}, Name: {car[1]}, Brand: {car[2]}, Model: {car[3]}, Year: {car[4]}, Color: {car[5]}, Filial: {car[6]}, Created At: {car[7]}")

    @log_decorator
    def show_all_cars(self):
        """
        Show all cars in the car table.
        """
        query = "SELECT * FROM car;"
        result = execute_query(query, fetch="all")
        print("Cars:")
        for car in result:
            print(
                f"- ID: {car[0]}, Name: {car[1]}, Brand: {car[2]}, Model: {car[3]}, Year: {car[4]}, Color: {car[5]}, Filial: {car[6]}, Created At: {car[7]}")
