import threading

from main_files.decorator.decorator_func import log_decorator
from page.auth.auth import Auth
from role.super_admin.sup_admin import Super_admin


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
5. Search filial by name
5. logout
    """)
    choice = input("Choose menu: ")
    sup_admin = Super_admin()
    if choice == '1':
        print("Add new filial")
        sup_admin.add_filial()
        filial_menu_for_sup_admin()
    elif choice == '2':
        print("Update filial")
        sup_admin.update_filial()
        filial_menu_for_sup_admin()
    elif choice == '3':
        print("Delete filial")
        sup_admin.delete_filial()
        filial_menu_for_sup_admin()
    elif choice == '4':
        print("Show all filial")
        sup_admin.show_filials()
        filial_menu_for_sup_admin()
    elif choice == '5':
        sup_admin.search_filial()
        filial_menu_for_sup_admin()
    elif choice == '6':
        print("Good bye!")
        auth.logout()


if __name__ == '__main__':
    auth = Auth()
    threading.Thread(target=auth.logout).start()
    filial_menu_for_sup_admin()
