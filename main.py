import threading

from main_files.decorator.decorator_func import log_decorator

from page.auth.auth import Auth

from role.filial_manager.color import ColorManager
from role.filial_manager.manager import CarsManager
from role.filial_manager.model import ModelManager
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

@log_decorator
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
    print('''
1. Add new color
2. Show all colors
3. Back
    ''')
    choice = input("Choose menu: ")
    color_manager = ColorManager()
    if choice == '1':
        print("Add new color")
        color_manager.add_car_color()
        color_menu()
    elif choice == '2':
        print("Show all colors")
        color_manager.show_car_colors()
        color_menu()
    elif choice == '3':
        print("Back")
        managers_menu()
    else:
        print("Invalid input")
        color_menu()


@log_decorator
def model_menu():
    print("""
1. Add new model
2. Show all models
    """)
    choice = input("Choose menu: ")
    model_manager = ModelManager()
    if choice == '1':
        print("Add new model")
        model_manager.add_car_model()
        model_menu()
    elif choice == '2':
        print("Show all models")
        model_manager.show_all_model()
        model_menu()
    else:
        print("Invalid input")
        model_menu()

@log_decorator
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
    cars_manager = CarsManager()
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
        cars_manager.search_car()
        cars_menu()
    elif choice == '6':
        print("Logout")
        managers_menu()


# def customer_menu():
#     print("""
# 1. Add new customer
# 2. Update customer information
# 3. Delete customer information
# 4. Show all customer
# 5. Search customer by name
# 6. logout
#     """)
#     choice = input("Choose menu: ")
#     customer = CostumerManager()
#     if choice == '1':
#         print("Add new customer")
#         customer.add_customer()
#         customer_menu()
#     elif choice == '2':
#         print("Update customer information")
#         customer.update_customer()
#         customer_menu()
#     elif choice == '3':
#         print("Delete customer information")
#         customer.delete_customer()
#         customer_menu()
#     elif choice == '4':
#         print("Show all customer")
#         customer.show_customers()
#         customer_menu()
#     elif choice == '5':
#         print("Search customer by name")
#         customer.search_customer()
#         customer_menu()
#     elif choice == '6':
#         print("Logout")
#         managers_menu()

@log_decorator
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
    color_menu()
