# data.py
# Static data used by the application.

MENU = {
    "Burger": {"price": 150.0, "category": "Main Course"},
    "Pizza": {"price": 300.0, "category": "Main Course"},
    "Pasta": {"price": 220.0, "category": "Main Course"},
    "Coffee": {"price": 100.0, "category": "Beverage"},
    "Brownie": {"price": 120.0, "category": "Dessert"},
}

# Tuple: fixed tax/discount configuration.
BILLING_RULES = (0.05, 0.10, 0.15)  # tax rate, standard discount, high discount

# Set: categories available in the restaurant.
CATEGORIES = {"Main Course", "Beverage", "Dessert"}
