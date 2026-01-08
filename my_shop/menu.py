import manager as m
from storage import Storage


def run_menu():
    my_storage = Storage()

    while True:

        m.main_menu()
        choice = input("Enter your choice: ")

        try:
            choice = int(choice)
            if choice == 3:
                print("Bye! Have a good day!")
                break

            elif choice == 1:
                while True:
                    m.cash_regicter()
                    choice2 = input("Enter your choice: ")
                    try:
                        choice2 = int(choice2)

                        if choice2 == 3:
                            print("Backing to Main Menu..")
                            break

                        elif choice2 == 1:
                            print("New Sale")
                            break
                        elif choice2 == 2:
                            print("Shift Report")
                            break
                        else:
                            print("Invalid choice")
                            continue

                    except ValueError:
                        print('Invalid choice')
                        continue

            elif choice == 2:
                while True:
                    m.management_menu()
                    choice3 = input("Enter your choice: ")

                    try:
                        choice3 = int(choice3)
                        if choice3 == 5:
                            print("Backing to Main Menu..")
                            break


                        elif choice3 == 1:
                            print("Adding a product to sale..")
                            name = input("Enter product name: ")
                            price = float(input("Enter product price: "))
                            quantity = int(input("Enter product quantity: "))
                            my_storage.add_product(name, price, quantity)
                            break
                        elif choice3 == 2:
                            print("Removing a product from sale..")
                            name = input("Enter product name: ")
                            my_storage.remove_product(name)
                            break
                        elif choice3 == 3:
                            print("Changing the product quantity..")
                            name = input("Enter product name: ")
                            quantity = int(input("Enter product quantity: "))
                            my_storage.restock_product(name, quantity)
                            break
                        elif choice3 == 4:
                            print("Displaying a balance report..")
                            products = my_storage.get_all_products()
                            for product in products:
                                print(product)

                            break
                        else:
                            print("Invalid choice")
                            continue

                    except ValueError:
                        print('Invalid choice')
                        continue


            else:
                print('Invalid choice')
                continue

        except ValueError:
            print('Invalid choice')
            continue



run_menu()
