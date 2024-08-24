import threading

from main_files.database.db_setting import Database, execute_query
from main_files.decorator.decorator_func import log_decorator
from psycopg2 import sql


class CostumerManager:
    def __init__(self):
        self.db = Database()


    @log_decorator
    def create_customer_table(self):
        """
        Create the customers table in the database if it does not already exist.
        """
        query = '''
            CREATE TABLE IF NOT EXISTS customers (
            ID SERIAL PRIMARY KEY,
            first_name VARCHAR(64) NOT NULL,
            last_name VARCHAR(64) NOT NULL,
            phone_number VARCHAR(64) NOT NULL,
            gmail VARCHAR(64) NOT NULL,
            CREATED_AT TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
            );
        '''
        with self.db as cursor:
            cursor.execute(query)
            return None


    @log_decorator
    def add_customer(self):
        """
        Add a new customer to the customers table.
        """
        threading.Thread(target=self.create_customer_table).start()
        first_name = input("Customer first name: ").strip()
        last_name = input("Customer last name: ").strip()
        phone_number = input("Customer phone number: ").strip()
        gmail = input("Customer gmail: ").strip()
        query = '''INSERT INTO customers (first_name, last_name, phone_number, gmail) VALUES (%s, %s, %s, %s);'''
        params = (first_name, last_name, phone_number, gmail)
        threading.Thread(target=execute_query, args=(query, params)).start()
        print(f"Customer '{first_name} {last_name}' added successfully.")
        return None


    @log_decorator
    def update_customer(self):
        """
        Update the name and address of a customer in the customers table.
        """
        customer_id = int(input("Customer ID: "))
        first_name = input("New Customer first name: ")
        last_name = input("New Customer last name: ")
        phone_number = input("New Customer phone number: ")
        gmail = input("New Customer gmail: ")
        execute_query(
            query="UPDATE customers SET first_name=%s, last_name=%s, phone_number=%s, gmail=%s WHERE ID=%s",
            params=(first_name, last_name, phone_number, gmail, customer_id)
        )
        print(f"Customer ID {customer_id} updated successfully.")
        return None

