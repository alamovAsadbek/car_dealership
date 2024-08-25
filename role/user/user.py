import hashlib
from main_files.database.db_setting import Database, execute_query
from main_files.decorator.decorator_func import log_decorator


class UserManager:
    def __init__(self):
        self.db = Database()

<<<<<<< HEAD

    def show_my_bought_cars(self):
            """
            Show my bought cars in the cars table.
            """
            query = "SELECT * FROM car WHERE STATUS SOLD "
            result = execute_query(query, fetch="all")
            print("Boght Cars:")
            for car in result:
                print(f"- ID: {car[0]}, Name: {car[1]}, Year: {car[2]}, Model_ID: {car[3]}, Color_ID: {car[4]}, Filial_ID: {car[5]}, Status: {car[6]}, Created_at : {car[7]}")
            return None
=======
    def show_my_bought_cars(self):
        """
        Show my bought cars in the cars table.
        """
        query = "SELECT * FROM car WHERE STATUS SOLD "
        result = execute_query(query, fetch="all")
        print("Boght Cars:")
        for car in result:
            print(
                f"- ID: {car[0]}, Name: {car[1]}, Year: {car[2]}, Model_ID: {car[3]}, Color_ID: {car[4]}, Filial_ID: {car[5]}, Status: {car[6]}, Created_at : {car[7]}")
        return None
>>>>>>> 76384d4859966cef580ad4cd69245178f50b3e77
