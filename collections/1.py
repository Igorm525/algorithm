# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала для каждого.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.


def avg(items):
    return sum(items) / len(items)


quantity = int(input("Количество предприятий: "))
companies = {}
for _ in range(quantity):
    name = input("Название предприятия: ")
    companies[name] = [int(input(f"Прибыль за {i+1}-ый квартал: ")) for i in range(4)]

average = avg([avg(company[1]) for company in companies.items()])

less_more = ([], [])
for name, value in companies.items():
    average_company = avg(value)
    less_more[average_company > average].append({name: average_company})

print(f'Средняя прибыль (за год для всех предприятий) {average}')
print(f'Предприятия с прибылью ниже среднего {less_more[0]}')
print(f'Предприятия с прибылью выше среднего {less_more[1]}')

