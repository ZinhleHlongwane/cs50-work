import string

text = input("Enter text: ")
punctuations = string.punctuation
result = ""

for char in text:
    if char not in punctuations:
        result = result + char

print(result)