text = input("Enter text: ")
result = ""
count = 0

for char in text:
    if char.isalpha():
        if count % 2 == 0:
            result = result + char.lower()
        else:
            result = result + char.upper()
        count = count + 1
    else:
        result = result + char

print(result)
