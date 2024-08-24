import threading

from main_files.decorator.decorator_func import log_decorator
from page.auth.auth import Auth


@log_decorator
def auth_menu():
    text = '''
1. Login
2. Logout
    '''
    print(text)
    try:
        user_input: int = int(input("Choose menu: "))
        if user_input == 1:
            result_login = auth.login()
            if not result_login['is_login']:
                auth_menu()
        elif user_input == 2:
            print("Good bye!")
        else:
            print("Invalid input")
            auth_menu()
    except Exception as e:
        print(f'Error: {e}')
        auth_menu()


if __name__ == '__main__':
    auth = Auth()
    threading.Thread(target=auth.logout).start()
    auth_menu()
