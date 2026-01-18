card_num = input("Enter credit card number: ")
result = ""

for i in range(1, card_num + 1):
    if i == len(16) and i == len(12):
        result = result + "*"