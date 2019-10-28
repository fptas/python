

value = -1
while value <= 0:
    value = int(input("Enter a positive number: "))

mind = -1
while value > 0:
    d = value % 10
    if d > mind:
        mind = d
    value = value // 10

print(f"Highest digit is: {mind}")