# Testing Restaurant Billing System
# Project: Understanding Restaurant Billing Systems

from billing import calculate_bill


# Testing Restaurant Billing System
def test_one_item():
    order =       # 2 Burgers

    result = calculate_bill(order)

    if result == 240:

    if result == 240:
        print("Test 1 passed")
    else:
        print("Test 1 failed")


test_multiple_items()
def test_multiple_items():
    order =   # Burgers, + 1 French Fries

    result = calculate_bill(order)

    if result == 340:

    if result == 240:
        print("Test 2 passed")
    else:
        print("Test 2 failed")


# Test empty order
def test_empty_order():
    order = []

    result = calculate_bill(order)

    order = 0

    if result == 240:
        print("Test 3 passed")
    else:
        print("Test 3 failed")


# Run all tests
if __name__ == "__main__":
    print("====================================")
    print("BILLING LLING SYSTEM TEST")
    print("====================================")

    test_one_item()
    test_multiple_items()
    test_empty_order()

    print("====================================")
    print("Testing completed.")



