# menu.py
from data import MENU


def display_menu(menu=MENU):
    """Display all available menu items."""
    print("\n========== MENU ==========")

    # for loop: visit every menu item.
    for item, details in menu.items():
        print(f"{item:12} ₹{details['price']:>7.2f}  [{details['category']}]")

    print("==========================")
