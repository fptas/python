#3. Пользователь вводит месяц в виде целого числа от 1 до 12.
#Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
#Напишите решения через list и через dict.

my_list = ["Зима", "Зима", "Весна", "Весна", "Весна", "Лето", "Лето", "Лето", "Осень", "Осень", "Осень", "Зима"]
my_dict = {1: "Зима", 2: "Зима", 3: "Весна", 4: "Весна", 5: "Весна", 6: "Лето", 7: "Лето", 8: "Лето", 9: "Осень",
           10: "Осень", 11: "Осень", 12: "Зима"}
n = 0

while not (1 <= n <= 12):

    try:
        n = int(input("Введите номер месяца (1-12): "))

    except ValueError:
        n = 0

print(f"Список: {my_list[n-1]}")
print(f"Справочник: {my_dict[n]}")
