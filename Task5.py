

income = float(input("Enter company income: "))
spending = float(input("Enter company spending: "))

if income > spending:
    print(f"income {income} > spending {spending}: profit = {income-spending}")
    numworkers = int(input("Enter number of workers: "))
    print(f"profit per worker is {((income - spending)/numworkers):.2f}")
elif  income < spending:
    print(f"income {income} < spending {spending}: loss = {spending - income}")
else:
    print(f"income {income} = spending {spending}")
