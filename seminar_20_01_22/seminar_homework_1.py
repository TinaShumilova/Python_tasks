# 1. По двум заданным числам проверять является ли первое квадратом второго
# def Task_1(x,y):
#     return x == y**2

# a = int(input('a = '))
# b = int(input('b = '))
# print(Task_1(a, b))

 #3. По заданному номеру дня недели вывести его название
# def day_title(x):
#     titles = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
#     if 0 < x < 8:
#         x -= 1
#         return titles[x]
#     else: return 'Неверно выбранный день недели.'

# c = int(input('Введите номер дня недели - '))
# print(day_title(c))

#5. Написать программу вычисления значения функции y = f(a)
import math

def find_cosinus(x):
    return f'cos{x} = {math.cos(x)}'

d = int(input('число = '))
print(find_cosinus(d))


        