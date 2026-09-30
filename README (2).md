# Project Title - Canteen Billing System
# Project Overview
* I built this basic Canteen Billing System using Python to manage customer details, food orders, billing, and payments inside a college canteen.
* The project is divided into separate Python modules, where each module performs a specific task.
* The system takes customer details, displays the food menu, records food orders, calculates the total bill, processes payment, and prints the final receipt.
* The project runs locally using Python and does not require any internet connection or cloud service.

# Features

* Customer Details - Takes customer name and phone number.
* Customer Validation - Checks whether the entered customer details are valid.
* Food Menu - Displays available food items and their prices.
* Order Management - Allows the customer to select food items and quantities.
* Bill Calculation - Calculates the total amount based on selected items and quantities.
* Payment Processing - Allows the user to select a payment method.
* Receipt Generation - Prints the final bill after successful payment.
* Invalid Input Handling - Displays an error message for invalid inputs.
* New Customer - Allows the user to start a new order after completing a bill.
* Exit Option - Allows the user to safely exit the system.

# Technologies Used

* Python 3
* Jupyter Notebook
* Google Colab
* Python Modules
* Functions
* Lists
* Dictionaries
* Loops
* Conditional Statements
* Input Validation

# Project Files

1. `main.py` - Controls the complete program flow.
2. `customer_details.py` - Takes and validates customer details.
3. `food_menu.py` - Displays the available food items and prices.
4. `order.py` - Takes food orders and quantities.
5. `bill.py` - Calculates the total bill amount.
6. `payment.py` - Handles the payment method.
7. `print_bill.py` - Prints the final bill and receipt.

# Running the App

To run the project on your computer, open Jupyter Notebook or a terminal, go to the project folder, and run the main program.

```bash
python main.py
```

## Test Phase 1: Customer Details Input

* Action: Run `main.py` and enter the customer name and phone number.
* Constraint Checked: Customer details input and validation.
* Test Input:
    * Name: `Rahul`
    * Phone: `9513574268`

<img width="397" height="367" alt="image" src="https://github.com/user-attachments/assets/db0b4a41-c143-4065-8023-354a4845820f" />

## Test Phase 2: Food Menu Display

* Action: Continue after entering valid customer details.
* Constraint Checked: Food menu display.
* System Response: The system displays the available food items along with their prices.
  
<img width="397" height="287" alt="image" src="https://github.com/user-attachments/assets/05e7317f-ba59-460d-95b8-4ec5b096bc66" />



## Test Phase 3: Order Entry

* Action: Select a food item and enter the required quantity.
* Constraint Checked: Food item selection and quantity input.
* Test Input:
    * Food Item: `Burger`
    * Quantity: `2`
* System Response: The selected food item and quantity are added to the customer's order.

<img width="410" height="276" alt="image" src="https://github.com/user-attachments/assets/904f27af-a45f-4281-97cc-d6dc855061d6" />


## Test Phase 4: Bill Calculation

* Action: Complete the food order.
* Constraint Checked: Item-wise amount and total bill calculation.
* System Response: The system calculates and displays the correct total bill.

<img width="467" height="251" alt="image" src="https://github.com/user-attachments/assets/5afbfe3e-331e-4a00-a7d0-50de1eb28c16" />


## Test Phase 5: Payment Processing

* Action: Select a payment method after calculating the bill.
* Constraint Checked: Payment method selection.
* Test Input:
    * Payment Method: `UPI`
* System Response: The system accepts the selected payment method and proceeds to the final bill.

<img width="436" height="260" alt="image" src="https://github.com/user-attachments/assets/ec2ff5b1-c437-4b9d-a73d-0e7dc473922f" />


## Test Phase 6: Final Receipt Verification

* Action: Complete the payment process.
* Constraint Checked: Final receipt generation.
* System Response: The system prints the final receipt containing customer details, ordered items, quantity, total bill, and payment method.

<img width="507" height="415" alt="image" src="https://github.com/user-attachments/assets/44e97e48-1a28-40b8-8f08-17fdcd594782" />

## Test Phase 7: Add New Customer

* Action: After completing the order, select `Add New Customer`.
* Constraint Checked: New customer flow.
* System Response: The system starts the customer details process again.


<img width="421" height="282" alt="image" src="https://github.com/user-attachments/assets/362d7072-2186-4722-86f7-dd7677caa1c0" />


## Test Phase 8: Invalid Main Menu Option

* Action: Enter an option that does not exist in the main menu, such as `5`.
* Constraint Checked: Main menu input validation.
* System Response: The system displays an invalid input message and shows the menu again.


<img width="432" height="230" alt="image" src="https://github.com/user-attachments/assets/2aaa344f-7438-4978-85b7-f6857d768478" />


## Test Phase 9: Exit System

* Action: Select `Exit` from the main menu.
* Constraint Checked: Program termination.
* System Response: The system displays the thank-you message and terminates safely.


<img width="417" height="205" alt="image" src="https://github.com/user-attachments/assets/865bd9da-babd-4f74-bb97-35dda0ac671f" />

