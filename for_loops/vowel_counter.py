text = input("Enter a string: ")

vowels = "AEIOUaeiou"

count = 0

for char in text:
    if char in vowels:
        count = count + 1

print(count)