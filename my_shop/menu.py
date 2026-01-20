import manager as m
from storage import Storage
import logging
from logging_config import setup_log



def run_menu():
    setup_log()
    my_storage = Storage()
    logging.info("App started")

    while True:

        m.main_menu()
        logging.info("Main_menu started")
        choice = input("Enter your choice: ")


        try:
            choice = int(choice)

        except ValueError:
            print('Invalid menu choice')
            logging.warning("Invalid choice in main menu")
            continue

        if choice == 3:
                print("Bye! Have a good day!")
                logging.info("Main menu closed by user")
                break

        elif choice == 1:
            # Cash register
            while True:
                m.cash_register()
                logging.info("Cash register started")
                choice2 = input("Enter your choice: ")

                try:
                    choice2 = int(choice2)
                except ValueError:
                    print('Invalid choice')
                    logging.warning("Invalid choice in cash register")
                    continue

                if choice2 == 3:
                    print("Backing to Main Menu..")
                    logging.info("Cash register closed by user, return to main menu")
                    break

                elif choice2 == 1:
                    print("New Sale")
                    products = my_storage.get_all_products()
                    if len(products) == 0:
                        print("No products in sale")
                        print("Backing to Main Menu..")
                        break
                    for product in products:
                        print(product)

                    name = input("Enter product name: ")
                    try:
                        quantity = int(input("Enter product quantity: "))
                        sale = my_storage.sell_product(name, quantity)
                        my_storage.save_sale_to_file(sale)
                        print(f"Total price: {sale['total']} dollars")
                        logging.info(f"New sale of{name} completed")
                    except ValueError as e:
                        print(e)
                        logging.warning(e)

                elif choice2 == 2:
                    print("Shift Report")
                    my_storage.shift_report()
                    break
                else:
                    print("Invalid choice")
                    logging.warning("Invalid choice in cash register")
                    continue


        elif choice == 2:
            # Management menu
            while True:
                m.management_menu()
                logging.info("Management menu started")
                choice3 = input("Enter your choice: ")

                try:
                    choice3 = int(choice3)
                except ValueError:
                        print('Invalid choice')
                        logging.warning("Invalid choice in management menu")
                        continue

                if choice3 == 5:
                    print("Backing to Main Menu..")
                    logging.info("Management menu closed by user, return to main menu")
                    break


                elif choice3 == 1:
                    try:
                        print("Adding a product to sale..")
                        name = input("Enter product name: ")
                        price = float(input("Enter product price: "))
                        quantity = int(input("Enter product quantity: "))
                        my_storage.add_product(name, price, quantity)
                        logging.info(f"Product added: {name}")
                    except ValueError as e:
                        print(e)
                        logging.warning(e)

                elif choice3 == 2:
                    try:
                        print("Removing a product from sale..")
                        name = input("Enter product name: ")
                        my_storage.remove_product(name)
                        logging.info(f"Product removed: {name}")
                    except ValueError as e:
                        print(e)
                        logging.warning(e)

                elif choice3 == 3:
                    try:
                        name = input("Enter product name: ")
                        quantity = int(input("Enter product quantity: "))
                        my_storage.restock_product(name, quantity)
                        logging.info(f"Product restocked: {name}, +{quantity}")
                    except ValueError as e:
                        print(e)
                        logging.warning(e)

                elif choice3 == 4:
                    print("Displaying a balance report..")
                    products = my_storage.get_all_products()
                    if len(products) == 0:
                        print("No products in sale")
                    for product in products:
                        print(product)

                    break
                else:
                    print("Invalid choice")
                    logging.warning("Invalid choice in management menu")
                    continue

        else:
            print('Invalid choice')
            logging.warning("Invalid choice in main menu")
            continue



run_menu()
