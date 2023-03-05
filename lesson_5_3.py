# 3) Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и
# величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
# 20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода
# сотрудников.


summ_salary = 0
with open("test_file_5_3.txt", encoding='utf-8') as my_file:
    employees = my_file.readlines()

for employee in employees:
    name, salary = employee.split()
    salary = float(salary)
    summ_salary += salary
    if salary < 20000:
        print(f"Employees with a salary of less than 20000: {name}")
print('Average salary: ', round(summ_salary / len(employees), 2))
