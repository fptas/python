from sys import argv

if len(argv) != 4:
    print("Необходимо указать 3 параметра!")
else:
    first_param, second_param, third_param = map(int, argv[1:])
    print(f"Заработная плата составляет: {first_param} * {second_param} + {third_param} = {first_param * second_param + third_param}")


