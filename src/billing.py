# Restaurant Billing System
# Project: Understanding Restaurant Billing Systems

print("====================================")
print("       WELCOME TO OUR RESTAURANT")
print("====================================")

# Menu
menu = {
    1: ("Burger", 120),
    2: ("Pizza", 250),
    3: ("Pasta", 180),
    4: ("French Fries", 100),
    5: ("Cold Drink", 60),
    6: ("Ice Cream", 80)
}

print("\n----------- MENU -----------")

for number, item in menu.items():
    print(number, ".", item[0], "- Rs.", item[1])

print("----------------------------")


# Function to calculate the bill
def calculate_bill(order):
    total = 0

    for item_number, quantity in order:
        item_name = menu[item_number][0]
        price = menu[item_number][1]

        item_total = price * quantity
        total = total + item_total

        print(item_name, "x", quantity, "=", item_total)

    return total


# Taking customer's order
order = []

while True:
    choice = int(input("\nEnter item number (0 to finish): "))

    if choice == 0:
        break

    if choice in menu:
        quantity = int(input("Enter quantity: "))

        if quantity > 0:
            order.append((choice, quantity))
        else:
            print("Please enter a valid quantity.")
    else:
        print("Invalid item number. Please try again.")


# Generate bill
print("\n====================================")
print("             BILL")
print("====================================")

if len(order) == 0:
    print("No items were ordered.")
else:
    subtotal = calculate_bill(order)

    # Tax
    gst = subtotal * 0.05

    # Final amount
    final_amount = subtotal + gst

    print("------------------------------------")
    print("Subtotal       : Rs.", round(subtotal, 2))
    print("GST (5%)       : Rs.", round(gst, 2))
    print("------------------------------------")
    print("Total Amount   : Rs.", round(final_amount, 2))
    print("====================================")
    print("       Thank you for visiting!")
    print("====================================")