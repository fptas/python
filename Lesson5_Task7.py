"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки. Необходимо вычислить прибыль каждой компании и среднюю прибыль.
Реализовать список, содержащий словарь (название фирмы и прибыль) и словарь с одним элементом (средняя прибыль).
Добавить в первый словарь еще один элемент, содержащий результат вычисления отношения прибыли к убыткам.
Итоговый список сохранить в файл.
"""


mydict1 = {}
mydict2 = {}
with open("Task7_in.txt", "r") as fobj:
    for line in fobj:
        name, type, revenue, costs = line.split()
        revenue, costs = float(revenue), float(costs)
        profit = revenue - costs
        mydict1[name] = profit

#average_profit
mydict2["average_profit"] = sum([i for i in mydict1.values() if i > 0])
mlist = [mydict1, mydict2]
with open("Task7_out.txt", "w") as fobj:
    print(mlist, file = fobj, end = '')