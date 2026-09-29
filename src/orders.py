'''
# Restaurant Order System
# Project: Understanding Restaurant Billing Systems 

# Importing the menu from menu.py '''
from menu import menu


# Function to take customer's order
def take_order():
    order = []

    print("\n====================================")
    print("          PLACE YOUR ORDER")
    print("====================================")

    while True:
        choice = int(input("Enter item number (0 to finish): "))

        # Stop taking the order
        if choice == 0:
            break

        # Check if item is available
        
    if choice in menu:
        while True:
            try:
               quantity = int(input("Enter quantity: "))

               if quantity > 0:
                   break
               else:
                   print("Please enter a quantity greater than 0.")


            except ValueError:
                   print("Please enter a valid number.")

    if quantity > 0:
        order.append((choice, quantity))
        print("Item added to order.")
    else:
        print("Please enter a valid quantity.") 


    return order


# Function to display the order
def display_order(order):
    print("\n====================================")
    print("             YOUR ORDER")
    print("====================================")

    if len(order) == 0:
        print("No items ordered.")
    else:
        for item_number, quantity in order:
            item_name = menu[item_number][0]
            price = menu[item_number][1]

            total_price = price * quantity

            print(item_name, "x", quantity, "= Rs.", total_price)

    print("====================================")


# Run the program
if __name__ == "__main__":
    customer_order = take_order()
    display_order(customer_order)

