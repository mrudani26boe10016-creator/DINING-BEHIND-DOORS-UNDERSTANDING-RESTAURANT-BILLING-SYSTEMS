# orders.py
from validation import get_menu_item, get_positive_integer


def create_order(menu):
    """Create an order using menu items and quantities."""
    order = {}

    print("\nCreate Order")
    while True:
        item = get_menu_item(menu)

        if item is None:
            break

        quantity = get_positive_integer(f"Quantity for {item}: ")

        # Dictionary: item -> quantity.
        order[item] = order.get(item, 0) + quantity

        print(f"{quantity} x {item} added.")

    return order


def remove_item(order, item):
    """Remove an item from an order if it exists."""
    if item in order:
        del order[item]
        return True
    return False


def can_cancel(status):
    """Apply cancellation rules based on order status."""
    if status == "PENDING":
        return True
    elif status == "PREPARING":
        return False
    else:
        return False


def cancel_order(status):
    """Return the new status after a cancellation request."""
    if can_cancel(status):
        return "CANCELLED"
    return status


def unique_order_items(order):
    """Return unique ordered item names as a set."""
    return set(order.keys())
