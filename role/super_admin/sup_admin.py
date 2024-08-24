"""menu:
1. Add new filial
2. Update filial
3. Delete filial
4. Show all filial
    """
from main_files.database.db_setting import Database
from main_files.decorator.decorator_func import log_decorator


class Super_admin:
    def __init__(self):
        self.__database = None
        self.db = Database

    @log_decorator
    def create_filial_table(self):
        """
               Create the users table in the database if it does not already exist.
        """
        query = '''
            CREATE TABLE IF NOT EXISTS filials (
            ID SERIAL PRIMARY KEY,
            NAME VARCHAR(255) NOT NULL,
            ADDRESS VARCHAR(255) NOT NULL,
            CREATED_AT TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
            );
            '''
        with self.__database as cursor:
            cursor.execute(query)
        return True

    @log_decorator
    def add_filial(self):
        """
               Add a new filial to the filials table.
        """
        self.create_filial_table()
        name: str = input("Filial Name: ")
        self.db.execute_query(query="INSERT INTO filials (NAME) VALUES (%s)", params=(name,))
        print(f"Filial '{name}' added successfully.")
        return None

    @log_decorator
    def update_filial(self):
        """
               Update the name of a filial in the filials table.
        """
        filial_id: int = int(input("Enter filial ID to update: "))
        name: str = input("Enter new filial Name: ")
        addres: str = input("Enter new filial location: ")
        self.db.execute_query(query="UPDATE filials SET NAME=%s, ADDRESS=%s WHERE ID=%s",
                              params=(name, addres, filial_id))
        print(f"Filial with ID '{filial_id}' updated successfully.")
        return Noneg
