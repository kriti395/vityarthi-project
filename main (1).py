from main_menu import show_main_menu
from food_menu import get_food_menu, display_menu
from take_order import collect_order
from generate_bill import create_bill
from payment import process_payment, print_receipt
from user_customer import add_customer_and_bill

def run_system():
    while True:
        menu_choice = show_main_menu()

        if menu_choice == "1":

            menu_items = get_food_menu()
            add_customer_and_bill(menu_items, display_menu, collect_order, create_bill, process_payment, print_receipt)

        elif menu_choice == "0":
            print("")
            print("Exiting the system. Thank you!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    run_system()
