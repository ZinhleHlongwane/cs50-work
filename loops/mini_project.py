# 1️⃣ Ask the player where they want to go
user_choice = input("Where do you want to go? ")

# 2️⃣ Dictionary of locations and items
locations = {
    "forest": ["stick", "stone", "berry", "mushroom"],
    "cave": ["stone", "gold coin", "torch", "bat wing"],
    "river": ["fish", "stone", "driftwood", "water bottle"],
    "village": ["bread", "apple", "coin", "stick"],
    "mountain": ["rock", "feather", "stick", "rare gem"]
}

# 3️⃣ Check if the user entered a valid location
if user_choice in locations:
    # 4️⃣ Loop through the items in that location
    for item in locations[user_choice]:
        # here you can display the item and/or ask the player to pick it up
        print(item)  # just showing the item for now
else:
    print("That location does not exist!")
