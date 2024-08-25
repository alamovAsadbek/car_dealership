import threading

from main_files.database.db_setting import Database, execute_query
from main_files.decorator.decorator_func import log_decorator


class Admin:
    def __init__(self):
        self.db = Database()

    @log_decorator
    def create_manager_table(self):
        """
        Create the manager table in the database if it does not already exist.
        """
        query = """
            CREATE TABLE IF NOT EXISTS manager (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) UNIQUE NOT NULL,
                phone_number VARCHAR(255) UNIQUE NOT NULL,
                filial_id INTEGER REFERENCES filial(id),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """
        with self.db.execute(query):
            return None

    @log_decorator
    def add_manager(self):
        """
        Add a new manager to the database.
        """
        threading.Thread(target=self.create_manager_table).start()
        name = input("Manager Name: ").strip()
        email = input("Manager Email: ").strip()
        phone_number = input("Manager Phone Number: ").strip()
        filial_id = input("Filial ID: ")
        query = """INSERT INTO manager (name, email, phone_number, filial_id) VALUES (%s, %s, %s, %s);"""
        threading.Thread(target=execute_query, args=(query, (name, email, phone_number, filial_id))).start()
        print(f"Manager '{name}' added successfully.")
        return None
