from random import randint
from functools import reduce
k = 5

def mnogochlen(k):
    equation_str = reduce(lambda x,y:  x+y, [str(i) + '**x' \
    + str(randint(0, 100)) + ' + ' for i in range(k + 1)])
    print(equation_str)
    equation_str = equation_str.replace('0**x','')
    print(equation_str)
    equation_str = equation_str[-4: -len(equation_str) - 1: -1]
    equation_str += ' = 0'
    print(equation_str)
    return equation_str

#with open('seminar_03_02_22/ex53.txt', 'w') as file:
    file.write(mnogochlen(k))


def mnogochlen_2(k):
    equation_str = reduce(lambda x,y:  x+y, [str(randint(0, 100)) + 'x**' + str(i) \
    + '+' for i in range(k + 1)])
    equation_str = equation_str.replace('x**0','')
    equation_str = equation_str.split('+')
    equation_str.pop()
    equation_str.reverse()
    result = f'{equation_str[0]}'
    for i in range(1, len(equation_str)):result += f' + {equation_str[i]}'
    result += ' = 0'
    print(result)
    return result

#with open('seminar_03_02_22/ex53.txt', 'w') as file:
    file.write(mnogochlen_2(k))