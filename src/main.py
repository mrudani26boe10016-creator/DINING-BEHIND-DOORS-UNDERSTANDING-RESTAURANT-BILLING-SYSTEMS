# main.py
from data import MENU
from menu import display_menu
from orders import create_order, cancel_order, unique_order_items
from billing import calculate_bill, print_bill
from reports import generate_report, display_report


def show_main_menu():
    print("""
========== DINING BEHIND DOORS ==========
1. Display Menu
2. Create Order
3. Generate Report
4. Exit
==========================================
""")


def process_new_order(orders):
    """Create an order, then either complete or cancel it."""
    order = create_order(MENU)

    if not order:
        print("No items were added.")
        return

    print(f"Unique items in order: {unique_order_items(order)}")
    bill = calculate_bill(order, MENU)

    print("""
Order status:
1. Complete order
2. Cancel order
""")

    choice = input("Choose status: ").strip()

    if choice == "2":
        status = cancel_order("PENDING")
        print(f"Order has been {status.lower()}.")
        orders.append({
            "items": order,
            "total": bill["total"],
            "status": status,
        })

    elif choice == "1":
        status = "COMPLETED"
        print_bill(order, bill, MENU)
        orders.append({
            "items": order,
            "total": bill["total"],
            "status": status,
        })

    else:
        print("Invalid choice. Order was not recorded.")


def main():
    orders = []

    while True:
        show_main_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            display_menu(MENU)

        elif choice == "2":
            process_new_order(orders)

        elif choice == "3":
            report = generate_report(orders)
            display_report(report)

        elif choice == "4":
            print("Thank you for using Dining Behind Doors.")
            break

        else:
            print("Invalid option. Please choose 1-4.")


if __name__ == "__main__":
    main()
