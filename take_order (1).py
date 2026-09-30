
def collect_order(menu_items):
    print("")
    print("================================")
    print("          TAKE ORDER")
    print("================================")
    order_list = []
    while True:
        try:
            item_num = int(input("Enter item number (or 0 to finish): "))

            if item_num == 0:
                break

            if item_num not in menu_items:
                print("Invalid item number. Please try again.")
                continue

            qty = int(input("Enter quantity: "))

            if qty <= 0:
                print("Quantity must be greater than zero.")
                continue

            selected_item = menu_items[item_num]

            order_entry = {
                "item_id": item_num,
                "item_name": selected_item["item_name"],
                "item_price": selected_item["item_price"],
                "item_qty": qty,
                "item_total": selected_item["item_price"] * qty
            }

            order_list.append(order_entry)

            print(qty, "x", selected_item["item_name"], "added to order.")

        except ValueError:
            print("Please enter a valid number.")

    return order_list
