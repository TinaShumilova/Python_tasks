# 48. Найти корни квадратного уравнения Ax² + Bx + C = 0
# b. Используя дополнительные библиотеки*
def Urovnenie(a, b, c):
    D = b**2 - 4*a*c
    print(D)

    if D < 0: return print('NO')
    elif D == 0: return print(-b /(2*a))
    else:
        x1 = (-b + (D)**0.5)/(2*a)
        print(b)
        print(a)
        print(D)
        x2 = (-b -(D)**0.5)/ (2*a)
        print(b)
        print(a)
        print(D)
        return print(x1, x2)

a = 2
b = -5
c = 2
Urovnenie(a, b, c)