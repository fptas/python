"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""
mlist = []
salaries = []
with open("Task3.txt", "r") as fobj:
    for line in fobj:
        if len(line) == 0:
            continue
        surname, salary_s = line.split()
        salary = float(salary_s)
        salaries.append(salary)
        if salary > 20000:
            mlist.append(surname)

print(f"Сотруднки с зарплатой > 20000: {mlist}")
print(f"Средняя зарплата: {sum(salaries)/ len(salaries): 0.2f}")

