c = 300000000
try:
    m = int(input("Enter mass: "))
    E = m * c * 2
    print(E)
except ValueError:
    print("Enter an interger!!")