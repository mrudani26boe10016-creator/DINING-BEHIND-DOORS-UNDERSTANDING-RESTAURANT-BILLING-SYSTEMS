# reports.py

# Restaurant Reports
# Project: Understanding Restaurant Billing Systems

# This list stores the bills made by customers
bills = []


# Function to add a bill to the report
def add_bill(amount):
    bills.append(amount)


# Function to calculate total sales
def total_sales():
    total = 0

    for amount in bills:
        total = total + amount

    return total


# Function to display the report
def show_report():
    print("\n====================================")
    print("        RESTAURANT SALES REPORT")
    print("====================================")

    if len(bills) == 0:
        print("No bills have been made yet.")
    else:
        print("Number of bills :", len(bills))

        for i in range(len(bills)):
            print("Bill", i + 1, ": Rs.", bills[i])

        print("------------------------------------")
        print("Total Sales     : Rs.", total_sales())

    print("====================================")


# Sample bills for testing
if __name__ == "__main__":

    add_bill(357)
    add_bill(540)
    add_bill(280)

    show_report()

