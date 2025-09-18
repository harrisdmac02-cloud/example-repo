# List of items in menu
menu_steers = {"hot_dogs": 50.00,
               "sushi": 125.80,
               "braai plate": 90.00,
               "pap & wors": 50.00,
               "bar_one chocolate": 40.00,
               "yogurt": 40.50,
               "pasta": 86.90,
               "snoek fish": 69.30}

# Initialise the empty values
shopping_cart = []
total_price = 0

print("-----------MENU-------------")
for key, value in menu_steers.items():
    print(f"{key:10} : R{value:.2f}")
print("#############################")

# While loop that stores user input
while True:
    food = input("What food do you want to buy? (Press 'q' to quit) ").lower()
    if food == "q":
        break

    elif menu_steers.get(food) is not None:
        shopping_cart.append(food)

# can also be expressed as tota_price += menu.get(food)
for food in shopping_cart:
    total_price = total_price + menu_steers.get(food)
    print(food, end=" ")

print()
print(f"Total price: {total_price:.2f}")