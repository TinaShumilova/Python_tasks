import math

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
# def find_cosinus(x):
#     return f'cos{x} = {math.cos(x)}'

# d = int(input('число = '))
# print(find_cosinus(d))

#7. Показать числа от -N до N
def show_number(x, y):
    for i in range(x, y+1):
        print(i)

e = int(input('-N = '))
g = int(input('N = '))
show_number(e, g)




        