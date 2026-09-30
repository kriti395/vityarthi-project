
def create_bill(order_list):
    print("")
    print("================================")
    print("         GENERATE BILL")
    print("================================")

    tax_percent = 5
    bill_subtotal = 0
    for each_item in order_list:
        bill_subtotal = bill_subtotal + each_item["item_total"]

    bill_tax = bill_subtotal * tax_percent / 100
    bill_grand_total = bill_subtotal + bill_tax

    final_receipt = {
        "order_items": order_list,
        "subtotal": bill_subtotal,
        "tax_rate": tax_percent,
        "tax_amount": bill_tax,
        "total_amount": bill_grand_total
    }

    print("Item           Qty     Price     Amount")
    print("---------------------------------------------")

    for order_item in order_list:
        print(order_item["item_name"], " " * (15 - len(order_item["item_name"])),
              order_item["item_qty"], " " * (8 - len(str(order_item["item_qty"]))),
              "Rs.", order_item["item_price"], " " * (10 - len(str(order_item["item_price"]))),
              "Rs.", order_item["item_total"])

    print("---------------------------------------------")
    print("Subtotal        : Rs.", bill_subtotal)
    print("Tax (", tax_percent, "%)       : Rs.", bill_tax)
    print("Grand Total     : Rs.", bill_grand_total)

    return final_receipt
