# word = input("Enter a word: ").lower()
# result = ""

while True:
    word = input("Enter a word: ").lower()

    if word == word[::-1]:
        break
    else:
        print("No, that is not a palindrome!!")

print("It's a palindrome!!")