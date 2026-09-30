def get_food_menu():
    menu_items = {
        1: {"item_name": "Tea", "item_price": 15},
        2: {"item_name": "Coffee", "item_price": 25},
        3: {"item_name": "Samosa", "item_price": 20},
        4: {"item_name": "Sandwich", "item_price": 60},
        5: {"item_name": "Burger", "item_price": 100},
        6: {"item_name": "Pizza", "item_price": 150},
        7: {"item_name": "Pasta", "item_price": 120},
        8: {"item_name": "Cold Drink", "item_price": 40}
    }
    return menu_items
def display_menu(menu_items):
    print("")
    print("================================")
    print("           FOOD MENU")
    print("================================")
    print("Item No   Item Name           Price")
    print("----------------------------------------")
    print("1         Tea                 15")
    print("2         Coffee              25")
    print("3         Samosa              20")
    print("4         Sandwich            60")
    print("5         Burger              100")
    print("6         Pizza               150")
    print("7         Pasta               120")
    print("8         Cold Drink          40")
    print("----------------------------------------")
