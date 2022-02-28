from sympy.solvers import solve

from sympy import Symbol

#f(x) = -8x**2+3x+17

x = Symbol('x')

list1 = solve(-8*x**2 + 3*x + 17, x)

x1 = list1[0]
x2 = list1[1]
print(x1, x2)

import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-5, 5, 50)
y = -8*x**2 + 3*x + 17
# Построение графика
plt.title("Зависимости: y = -8*x**2 + 3*x + 17") # заголовок
plt.xlabel("x")         # ось абсцисс
plt.ylabel("y")    # ось ординат
plt.grid()              # включение отображение сетки
plt.plot(x, y)  # построение графика