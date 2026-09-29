# My billing system for my restaurant
# By Mrudani Yayati Pethe 
print("Welcome to my restaurant")

total_money = 0
good_orders = 0
bad_orders = 0

is_running = 1

while is_running == 1:
    print("")
    print("1. Menu")
    print("2. Order")
    print("3. Report")
    print("4. Exit")

    x = input("Pick a number: ")

    # MENU
    if x == "1":
        print("")
        print("1. Fries is $4")
        print("2. Pizza is $15")
        print("3. Pasta is $12")
        print("4. Ice Cream is $8")
        print("5. Burger is $10")
        print("6. Cold Drink is $6")

    # ORDER
    if x == "2":
        price = 0

        while True:
            print("")
            print("What would you like to order?")
            print("1. Fries - $4")
            print("2. Pizza - $15")
            print("3. Pasta - $12")
            print("4. Ice Cream - $8")
            print("5. Burger - $10")
            print("6. Cold Drink - $6")
            print("0. Finish Order")

            food1 = input("Pick a food number: ")

            if food1 == "0":
                break

            if food1 == "1":
                food_name = "Fries"
                item_price = 4

            elif food1 == "2":
                food_name = "Pizza"
                item_price = 15

            elif food1 == "3":
                food_name = "Pasta"
                item_price = 12

            elif food1 == "4":
                food_name = "Ice Cream"
                item_price = 8

            elif food1 == "5":
                food_name = "Burger"
                item_price = 10

            elif food1 == "6":
                food_name = "Cold Drink"
                item_price = 6

            else:
                print("Invalid food number.")
                continue

            quantity = int(input("How many do you want? "))

            item_total = item_price * quantity
            price = price + item_total

            print(food_name + " added to your order.")
            print("Current total is $" + str(price))

            food2 = input("Do you want another food? Type yes or no: ")

            if food2.lower() != "yes":
                break

        print("")
        print("Your total is $" + str(price))
        print("Type 1 to pay or 2 to cancel")

        pay = input("-> ")

        if pay == "1":
            print("Thank you!")
            total_money = total_money + price
            good_orders = good_orders + 1

        if pay == "2":
            print("Cancelled")
            bad_orders = bad_orders + 1

    # REPORT
    if x == "3":
        print("")
        print("Money made: $" + str(total_money))
        print("Good orders: " + str(good_orders))
        print("Bad orders: " + str(bad_orders))

    # EXIT
    if x == "4":
        is_running = 0

print("Restaurant closed.")