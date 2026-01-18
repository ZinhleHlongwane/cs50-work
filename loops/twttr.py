twttr = input("Enter text: ")
vowels = "AEIOUaeiou"

result = ""

for char in twttr:
    if char not in vowels:
        result = result + char

print(result)

