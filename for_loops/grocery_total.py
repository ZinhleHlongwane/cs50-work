# items = input("Enter grocery items: ").lower()

grocery_prices = {
    "milk": 3.99,
    "bread": 2.50,
    "eggs": 4.25,
    "apples": 1.20,
    "chicken_breast": 7.50,
    "rice": 5.00,
    "coffee": 12.99
}
total = 0

while True:
    item = input("Enter grocery items: ").lower()

    if item == "done":
        break

    if item in grocery_prices:
        total = total + grocery_prices[item]
    else:
        print("Sorry, item not found. Please try again")

print(f"Total: {total:.2f}")
