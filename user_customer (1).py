
all_customers = []
active_customer = None
order_list = []
final_receipt = None
last_receipt = None

def add_customer_and_bill(menu_items, display_menu, collect_order, create_bill, process_payment, print_receipt):
    """Add customer and directly process complete order"""
    global active_customer, order_list, final_receipt, last_receipt

    print("")
    print("================================")
    print("        CUSTOMER DETAILS")
    print("================================")


    customer_name = input("Enter customer name: ").strip()
        if name == "":
            print("Invalid input! Name cannot be empty.")
        elif not name.replace(" ", "").isalpha():
            print("Invalid input! Name should contain only alphabets and spaces.")
        else:
            break


while True:
        contact_number = input("Enter phone number (10 digits): ").strip()

        if contact_number.isdigit() and len(contact_number) == 10:
            break

        print("Please enter a valid 10-digit phone number.")


    customer_id = len(all_customers) + 1

    active_customer = {
        "cust_id": customer_id,
        "cust_name": customer_name,
        "cust_phone": contact_number
    }

    all_customers.append(active_customer)

    print("")
    print("Customer added successfully!")
    print("Customer ID:", active_customer['cust_id'])
    print("Name:", active_customer['cust_name'])
    print("Phone:", active_customer['cust_phone'])

    # ========== FOOD MENU ==========
    display_menu(menu_items)

    # ========== TAKE ORDER ==========
    order_list = collect_order(menu_items)

    if not order_list:
        print("No items ordered. Returning to Main Menu...")
        return

    # ========== GENERATE BILL ==========
    final_receipt = create_bill(order_list)

    # ========== PAYMENT ==========
    process_payment(final_receipt, active_customer)

    # Save for printing
    last_receipt = final_receipt

    # ========== PRINT BILL ==========
    print_receipt(last_receipt, active_customer)

    print("")
    print("Returning to Main Menu...")
