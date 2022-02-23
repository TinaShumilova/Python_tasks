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
def square_table(g):
    for i in range(1, g+1): 
        print(f'{i} >>> {i**2}')

G = int(input('Введите конечное число - '))
square_table(G)

# Результат 
# 1 >>> 1
# 2 >>> 4
# 3 >>> 9
# 4 >>> 16
# 5 >>> 25
# None - откуда это взялось?   

# 25. Найти сумму чисел от 1 до А
# def sum_find(h):
#     summa = 0
#     for i in range(1, h+1): 
#         summa += i
#     return summa

# H = int(input('Введите конечное число - '))
# print(sum_find(H))

# 27. Определить количество цифр в числе
# def lenght_of_number(j):
#     temp = list(str(j))
#     if j > 0: return len(temp)
#     else:
#         temp.pop(0)
#         return len(temp)

# J = int(input('Введите число - '))
# print(lenght_of_number(J))

# 29. Написать программу вычисления произведения чисел от 1 до N
# def result_of_numbers_multiplication(k):
#     temp = 1
#     for i in range(1, k+1): 
#         temp *= i
#     return temp

# K = int(input('Введите конечное число - '))
# print(result_of_numbers_multiplication(K))