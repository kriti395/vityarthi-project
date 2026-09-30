
from datetime import datetime

def process_payment(final_receipt, active_customer):
    print("")
    print("================================")
    print("           PAYMENT")
    print("================================")

    print("Customer:", active_customer['cust_name'])
    print("Phone:", active_customer['cust_phone'])
    print("Amount to pay: Rs.", final_receipt["total_amount"])

    while True:
        pay_method = input("Choose payment method (cash/upi/card): ").strip().lower()

        if pay_method in ["cash", "upi", "card"]:
            print("Payment method:", pay_method.upper())
            print("Payment successful!")
            break

        print("Invalid payment method. Please try again.")

def print_receipt(last_receipt, active_customer):
    print("")
    print("================================")
    print("           PRINT BILL")
    print("================================")

    print("")
    print("=============================================")
    print("              CANTEEN BILL")
    print("=============================================")
    print("Customer :", active_customer['cust_name'])
    print("Phone    :", active_customer['cust_phone'])

    current_time = datetime.now()
    formatted_date = current_time.strftime('%d-%m-%Y %H:%M')
    print("Date     :", formatted_date)
    print("---------------------------------------------")

    print("Item           Qty     Price     Amount")

    for receipt_item in last_receipt["order_items"]:
        print(receipt_item["item_name"], " " * (15 - len(receipt_item["item_name"])),
              receipt_item["item_qty"], " " * (8 - len(str(receipt_item["item_qty"]))),
              "Rs.", receipt_item["item_price"], " " * (10 - len(str(receipt_item["item_price"]))),
              "Rs.", receipt_item["item_total"])

    print("---------------------------------------------")
    print("Subtotal              : Rs.", last_receipt["subtotal"])
    print("Tax (", last_receipt["tax_rate"], "%)              : Rs.", last_receipt["tax_amount"])
    print("Grand Total           : Rs.", last_receipt["total_amount"])
    print("=============================================")
    print("        Thank you. Visit again!")
    print("=============================================")
