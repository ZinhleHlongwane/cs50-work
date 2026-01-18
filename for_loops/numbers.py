text = input("Enter text: ")
result = ""

for char in text:
    if char.isdigit():
        result = result + char

print(result)
