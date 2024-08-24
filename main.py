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
            auth.login()
            auth_menu()
        elif user_input == 2:
            pass
        else:
            print("Invalid input")
            auth_menu()
    except Exception as e:
        print(f'Error: {e}')
        auth_menu()


if __name__ == '__main__':
    auth = Auth()
    auth.logout()
