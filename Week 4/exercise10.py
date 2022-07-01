""""
Exercise 10: Salary
@Author : Eduardo Alarcón
@version: 1.0
"""
salary = 0
base_salary = float(input('What is your base salary? '))
if base_salary >= 1000:
    salary = base_salary
else:
    age = int(input('What is your seniority? '))
    if age >= 10:
        salary = base_salary*1.20
    else:
        salary = base_salary*1.05
print('The final salary of the worker is:\n%3i Euros' %salary)
