import threading

from main_files.database.db_setting import Database, execute_query
from main_files.decorator.decorator_func import log_decorator
from psycopg2 import sql

class Super_admin:
    def __init__(self):
        self.db = Database()

    @log_decorator
    def create_filial_table(self):
        """
        Create the filials table in the database if it does not already exist.
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
    def add_filial(self):
        """
        Add a new filial to the filials table.
        """
        threading.Thread(target=self.create_filial_table).start()
        name = input("Filial Name: ").strip()
        address = input("Filial Address: ").strip()
        query='''INSERT INTO filials (NAME, ADDRESS) VALUES (%s, %s);'''
        params=(name, address)
        threading.Thread(target=execute_query, args=(query, params)).start()
        print(f"Filial '{name}' added successfully.")
        return None

    @log_decorator
    def update_filial(self):
        """
        Update the name and address of a filial in the filials table.
        """
        filial_id = int(input("Filial ID: "))
        name = input("New Filial Name: ")
        address = input("New Filial Address: ")
        execute_query(
            query="UPDATE filials SET NAME=%s, ADDRESS=%s WHERE ID=%s",
            params=(name, address, filial_id)
        )
        print(f"Filial ID {filial_id} updated successfully.")
        return None

    @log_decorator
    def delete_filial(self):
        """
        Delete a filial from the filials table.
        """
        filial_id = int(input("Filial ID: "))
        execute_query(query="DELETE FROM filials WHERE ID=%s", params=(filial_id,))
        print(f"Filial ID {filial_id} deleted successfully.")
        return None

    @log_decorator
    def show_filials(self):
        """
        Show all filials in the filials table.
        """
        query = "SELECT * FROM filials;"
        result = execute_query(query, fetch="all")
        print("Filials:")
        for filial in result:
            print(f"- ID: {filial[0]}, Name: {filial[1]}, Address: {filial[2]}, Created At: {filial[3]}")
        return None

    @log_decorator
    def search_filial(self):
        """
        Search for filials by name in the filials table.
        """
        name = input("Filial Name: ")
        query = "SELECT * FROM filials WHERE NAME LIKE %s;"
        result = execute_query(query, params=("%" + name + "%",), fetch="all")
        print("Filials:")
        for filial in result:
            print(f"- ID: {filial[0]}, Name: {filial[1]}, Address: {filial[2]}, Created At: {filial[3]}")
        return None
