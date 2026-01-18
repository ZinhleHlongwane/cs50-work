camelCase = input("Enter name of variable: ")

snake_case = ""

for char in camelCase:
    if char.isupper():
        snake_case = snake_case + "_" + char.lower()
    else:
        snake_case = snake_case + char

print(snake_case)


