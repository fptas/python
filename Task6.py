a = float(input("Enter a: "))
b = float(input("Enter b: "))

nday = 1
sum = a
while True:
    print(f"Day {nday}: {sum:0.2f} km")
    if sum >= b:
        break
    nday += 1
    sum *= 1.1

print (f"On the {nday} day")

