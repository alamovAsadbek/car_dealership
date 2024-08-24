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
            auth.login()
            auth_menu()
        elif user_input == 2:
            print("Good bye!")
        else:
            print("Invalid input")
            auth_menu()
    except Exception as e:
        print(f'Error: {e}')
        auth_menu()


def filial_menu_for_sup_admin():
    print("""
1. Add new filial
2. Update filial
3. Delete filial
4. Show all filial
5. logout
    """)
    choice = input("Choose menu: ")
    if choice == '1':
        print("Add new filial")
        pass
    elif choice == '2':
        print("Update filial")
        pass
    elif choice == '3':
        print("Delete filial")
        pass
    elif choice == '4':
        print("Show all filial")
        pass
    elif choice == '5':
        print("Good bye!")
        auth.logout()


if __name__ == '__main__':
    auth = Auth()
    threading.Thread(target=auth.logout).start()
    auth_menu()
