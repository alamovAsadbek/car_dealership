from main_files.database.db_setting import Database


class Sales:
    def __init__(self):
        self.db = Database()

    def create_sales_table(self):

        """
        Create the sales table in the database if it does not already exist.
        """
        query = '''
            CREATE TABLE IF NOT EXISTS sales (
            ID SERIAL PRIMARY KEY,
            car_id BIGINT NOT NULL REFERENCES car(ID),
            customer_id BIGINT NOT NULL REFERENCES customers(ID),
            sale_price DECIMAL NOT NULL,
            sale_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
            );
        '''
        with self.db as cursor:
            cursor.execute(query)
            return None

def sell_car(self, car_id, customer_id, sale_price):
    """
    Sell a car by updating its status and recording the sale.

    """
    query_check = "SELECT STATUS FROM car WHERE STATUS = %s;"
    with self.db as cursor:
        cursor.execute(query_check, (car_id,))
        car_status = cursor.fetchone()
        if car_status is None:
            raise ValueError(f"Car with ID {car_id} does not exist.")
        if car_status[0] == 'SOLD':
            raise ValueError(f"Car with ID {car_id} is already sold.")

    query_update = "UPDATE car SET STATUS = 'SOLD' WHERE ID = %s;"
    with self.db as cursor:
        cursor.execute(query_update, (car_id,))
    query_insert = '''
        INSERT INTO sales (car_id, customer_id, sale_price)
        VALUES (%s, %s, %s);
    '''
    with self.db as cursor:
        cursor.execute(query_insert, (car_id, customer_id, sale_price))
        print(f"Car with ID {car_id} sold to customer with ID {customer_id} for {sale_price}.")
