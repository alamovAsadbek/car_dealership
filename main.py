import threading

from main_files.decorator.decorator_func import log_decorator
from page.auth.auth import Auth
from role.super_admin.sup_admin import Super_admin
from role.filial_manager.manager import FilialManager


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


def managers_menu():
    print("""
1. Show all information
2. Customer manager
3. Cars manager
4. Logout
    """)
    choice = input("Choose menu: ")
    if choice == '1':
        print("Show all information")
        pass
    elif choice == '2':
        print("Customer filial_manager")
        pass
    elif choice == '3':
        print("Cars filial_manager")
        cars_menu()
        managers_menu()
    elif choice == '4':
        print("Logout")
        managers_menu()


@log_decorator
def color_menu():
    text = '''
1. Add new color
2. Show all colors
3. Back
    '''
    print(text)


def cars_menu():
    print("""
1. Add new car
2. Update car information
3. Delete car information   
4. Show all cars
5. Search car by name
6. logout
    """)
    choice = input("Choose menu: ")
    cars_manager = FilialManager()
    if choice == '1':
        print("Add new car")
        cars_manager.add_car()
        cars_menu()
    elif choice == '2':
        print("Update car information")
        cars_manager.update_car()
        cars_menu()
    elif choice == '3':
        print("Delete car information")
        cars_manager.delete_car()
        cars_menu()
    elif choice == '4':
        print("Show all cars")
        cars_manager.show_all_cars()
        cars_menu()
    elif choice == '5':
        print("Search car by model")
        cars_manager.search_car_by_model()
        cars_menu()
    elif choice == '6':
        print("Logout")
        managers_menu()


def customer_menu():
    print("""
1. Add new customer
2. Update customer information
3. Delete customer information
4. Show all customer
5. Search customer by name
6. logout
    """)
    choice = input("Choose menu: ")
    customer = CostumerManager()
    if choice == '1':
        print("Add new customer")
        customer.add_customer()
        customer_menu()
    elif choice == '2':
        print("Update customer information")
        customer.update_customer()
        customer_menu()
    elif choice == '3':
        print("Delete customer information")
        customer.delete_customer()
        customer_menu()
    elif choice == '4':
        print("Show all customer")
        customer.show_customers()
        customer_menu()
    elif choice == '5':
        print("Search customer by name")
        customer.search_customer()
        customer_menu()
    elif choice == '6':
        print("Logout")
        managers_menu()


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
    auth_menu()
