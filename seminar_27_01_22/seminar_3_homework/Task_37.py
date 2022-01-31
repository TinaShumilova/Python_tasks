from random import randint

def List_N(a, b, c):
    list1 = []
    while len(list1) <= c:
        list1.append(randint(a, b))
    return list1

def multiplicy_with_positions(list1, position1, position2):
    return list1[position1] * list1[position2]

def Position(file_name, num):
    with open(file_name) as fp:
        lines = fp.readlines()
    return int(lines[num])

file_name = 'seminar_27_01_22/seminar_3_homework/file.txt'
# with open(file_name, 'w') as data:
#     data.write('5\n')
#     data.write('3\n')
#     data.write('1\n')
#     data.write('4')

list1 = List_N(-5, 5, 10)
print(list1)

num1 = int(input())
num2 = int(input())
position1 = Position(file_name, num1)
position2 = Position(file_name, num2)

print(multiplicy_with_positions(list1, position1, position2))
