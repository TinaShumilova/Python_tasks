# 17. По двум заданным числам проверять является ли одно квадратом другого
# def square_or_not(a, b):
#     if a == b**2: return f'Число {a} является квадратом числа {b}'
#     elif b == a **2: return f'Число {b} является квадратом числа {a}'
#     else: return 'Ни одно число не является квадратом второго'

# A = int(input('Введите число 1 - '))
# B = int(input('Введите число 2 - '))
# print(square_or_not(A, B))

# 19. Определить номер четверти плоскости, в которой находится точка с 
# координатами Х и У, причем X ≠ 0 и Y ≠ 0
# def find_quatro(c, d):
#     if c > 0 < d: return '1-ая четверть'
#     elif c < 0 < d: return '2-ая четверть'
#     elif c < 0 > d: return '3-ая четверть'
#     elif c > 0 > d: return '4-ая четверть'
#     else: return 'Неверно введены данные. X ≠ 0 и Y ≠ 0'
# C, D = 5, -3
# print(find_quatro(C, D))

# 21. Программа проверяет пятизначное число на палиндромом.
# def polindrom_or_not(e):
#     e = input('Введите пятизначное число - ')
#     temp1 = int(e)
#     if temp1 > 0: temp2 = list(e)
#     else:
#         temp2 = list(e)
#         temp2.pop(0)
#     while len(temp2) == 5:
#         for i in temp2:
#             if temp2[0] == temp2[-1] and temp2[1] == temp2[-2]:
#                 return f'Число {e} является палиндромом'
#             else: 
#                 return f'Число {e} не является палиндромом'
#     else: return 'Неверно задано число.'

# E = None
# print(polindrom_or_not(E))

# 23. Показать таблицу квадратов чисел от 1 до N 
# def square_table(g):
#     for i in range(1, g+1): 
#         print(f'{i} >>> {i**2}')

# G = int(input('Введите конечное число - '))
# print(square_table(G))

# 25. Найти сумму чисел от 1 до А
# 27. Определить количество цифр в числе
# 29. Написать программу вычисления произведения чисел от 1 до N

