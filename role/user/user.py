import hashlib
from main_files.database.db_setting import Database, execute_query
from main_files.decorator.decorator_func import log_decorator

class UserManager:
    def __init__(self):
        self.db = Database()

# @log_decorator
# def login(self):
#     """
#             Authenticate a user by checking their email and password.
#             Updates the user's login status to True upon successful login.
#     """
#     email: str = input("Email: ").strip()
#     password: str = hashlib.sha256(input("Password: ").strip().encode('utf-8')).hexdigest()
#     user = execute_query("SELECT * FROM users WHERE EMAIL=%s", (email,), fetch='one')
#     if user is None:
#         print("Login failed")
#         return False
#     elif user['password'] == password and user['email'] == email:
#         query = '''UPDATE users SET IS_LOGIN=%s WHERE EMAIL=%s;'''
#         params = (True, email)
#         with self.__database as db:
#             db.execute(query, params)
#             print('Login successful')
#             return True
#     return False