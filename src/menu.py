# Restaurant Menu
# Project: Understanding Restaurant Billing Systems

# Menu items with their prices
menu = {
    1: ("Burger", 120),
    2: ("Pizza", 250),
    3: ("Pasta", 180),
    4: ("French Fries", 100),
    5: ("Cold Drink", 60),
    6: ("Ice Cream", 80)
}


# Function to display the menu
def display_menu():
    print("\n====================================")
    print("          RESTAURANT MENU")
    print("====================================")

    for number, item in menu.items():
        print(number, ".", item[0], "- Rs.", item[1])

    print("====================================")


# Function to add a new item
def add_item(item_number, item_name, price):
    menu[item_number] = (item_name, price)
    print(item_name, "has been added to the menu.")


# Function to remove an item
def remove_item(item_number):
    if item_number in menu:
        removed_item = menu.pop(item_number)
        print(removed_item[0], "has been removed from the menu.")
    else:
        print("Item not found.")


# Display the menu when this file is run
if __name__ == "__main__":
    display_menu()
