k = 5
equation_str = reduce(lambda x,y:  x+y, [str(i) + '**x' + str(random.randint(0, 100)) + ' + ' for i in range(k + 1)])
print(equation_str)
equation_str = equation_str[-4: -len(equation_str) - 1: -1]
equation_str += ' = 0'
print(equation_str)
with open('ex53.txt', 'w') as file:
    file.write(equation_str)
