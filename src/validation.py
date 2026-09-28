# validation.py
def get_positive_integer(prompt):
    """Read and validate a positive integer."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_menu_item(menu):
    """Read an item name and return its canonical menu name."""
    while True:
        item = input("Enter item name (or 'done'): ").strip()

        if item.lower() == "done":
            return None

        for menu_item in menu:
            if menu_item.lower() == item.lower():
                return menu_item

        print("That item is not available. Please choose from the menu.")
