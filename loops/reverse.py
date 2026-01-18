text = input("Enter text: ").lower()
result = ""

for char in text:
    result = char + result

print(result)