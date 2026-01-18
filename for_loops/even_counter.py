num = int(input("Enter positive integer: "))
count = 0

for i in range(1, num + 1):
    if i > 0 and i % 2 == 0:
        count = count + 1

print(count)