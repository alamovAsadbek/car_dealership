import hashlib
import threading

from email_sender.email import send_mail
from main_files.database.db_setting import Database, execute_query
from main_files.decorator.decorator_func import log_decorator


class CustomerManager:
    def __init__(self):
        self.db = Database()

    @log_decorator
    def create_users_table(self):
        query = '''
            CREATE TABLE IF NOT EXISTS users (
            ID SERIAL PRIMARY KEY,
            first_name VARCHAR(64) NOT NULL,
            last_name VARCHAR(64) NOT NULL,
            phone_number VARCHAR(64) NOT NULL,
            role VARCHAR(64) NOT NULL DEFAULT 'customer',
            email VARCHAR(64) NOT NULL,
            password VARCHAR(255) UNIQUE NOT NULL,
            status VARCHAR(50) NOT NULL DEFAULT False,
            created_at TIMESTAMP DEFAULT DATE_TRUNC('minute', NOW())
            );
        '''
        with Database() as db:
            db.cursor.execute(query)

    @log_decorator
    def add_customer(self):
        threading.Thread(target=self.create_users_table).start()

        first_name = input("Customer first name: ").strip()
        last_name = input("Customer last name: ").strip()
        phone_number = input("Customer phone number: ").strip()
        email = input("Customer email: ").strip()
        password = input("Customer password: ").strip()
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        subject = "You logged in: "
        message = f"Login: {email}\nPassword: {password}\n"

        query = """
        INSERT INTO users (first_name, last_name, phone_number, email, password)
        VALUES (%s, %s, %s, %s, %s);
        """
        params = (first_name, last_name, phone_number, email, hashed_password)

        try:
            threading.Thread(target=send_mail, args=(email, subject, message)).start()
            threading.Thread(target=execute_query, args=(query, params)).start()

            print("Customer added successfully.")
        except Exception as e:
            print(f"Failed to add customer: {e}")
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

        try:
            execute_query(
                query="UPDATE users SET first_name=%s, last_name=%s, phone_number=%s, gmail=%s WHERE ID=%s",
                params=(first_name, last_name, phone_number, gmail, customer_id)
            )
            print(f"Customer ID {customer_id} updated successfully.")
        except Exception as e:
            print(f"Failed to update customer: {e}")
        return None

    @log_decorator
    def delete_customer(self):
        """
        Delete a customer from the customers table.
        """
        customer_id = int(input("Customer ID: "))
        try:
            execute_query(query="DELETE FROM users WHERE ID=%s", params=(customer_id,))
            print(f"Customer ID {customer_id} deleted successfully.")
        except Exception as e:
            print(f"Failed to delete customer: {e}")
        return None

    @log_decorator
    def change_my_password(self):
        """
        change a customer pasword from the customers table.
        """
        customer_id = int(input("Customer ID: "))
        customer_password = int(input("CUSTOMER NEW PASSWORD: "))
        hashed_password = hashlib.sha256(customer_password.encode()).hexdigest()
        try:
            execute_query(query="UPDATE users SET password=%s WHERE ID=%s",
                          params=(hashed_password, customer_id))
            print(f"Customer ID {customer_password} updated successfully.")
        except Exception as e:
            print(f"Failed to update customer password: {e}")
        return None

    @log_decorator
    def show_customers(self):
        """
        Show all customers in the customers table.
        """
        query = "SELECT * FROM users;"
        result = execute_query(query, fetch="all")
        if result:
            print("Customers:")
            for customer in result:
                print(f"""- ID: {customer[0]}, First name: {customer[1]}, Last name: {customer[2]}, 
                      Phone number: {customer[3]}, Gmail: {customer[4]}, Created At: {customer[5]}""")
        else:
            print("No customers found.")
        return None

    @log_decorator
    def search_customer(self):
        """
        Search for customer by gmail in the customers table.
        """
        gmail = input("Customer gmail: ")
        query = "SELECT * FROM users WHERE gmail LIKE %s;"
        result = execute_query(query, params=("%" + gmail + "%",), fetch="all")
        if result:
            print("Customers:")
            for customer in result:
                print(f"""- ID: {customer[0]}, First name: {customer[1]}, Last name: {customer[2]}, 
                      Phone number: {customer[3]}, Gmail: {customer[4]}, Created At: {customer[5]}""")
        else:
            print("No customers found.")
        return None
