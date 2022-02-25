#Найти НОК двух чисел
from math import gcd

a = int(input('Введите первое число - '))
b = int(input('Введите второе число - '))

def find_NOK(a, b):
    if a == 0 or b == 0: return 'На ноль делить нельзя!!!'
    else: return ((a*b)//gcd(a, b))

print(find_NOK(a, b))