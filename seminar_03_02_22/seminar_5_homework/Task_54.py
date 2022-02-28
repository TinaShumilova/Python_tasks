#Даны два файла в каждом из которых находится запись многочлена.
# Сформировать файл содержащий сумму многочленов.
from Task_53 import mnogochlen_2

# a = 4
# b = 5
file_54_1 = 'seminar_03_02_22/seminar_5_homework/ex54_1.txt'
file_54_2 = 'seminar_03_02_22/seminar_5_homework/ex54_2.txt'
file_54_3 = 'seminar_03_02_22/seminar_5_homework/ex54_3.txt'

#with open(file_54_1, 'w') as file_1:
#    file_1.write(mnogochlen_2(a))

#with open(file_54_2, 'w') as file_2:
#    file_2.write(mnogochlen_2(b))

first = ''
temp = open(file_54_1, 'r')
for i in temp: first += i
first = first.replace(' = 0', '')
first = first.split('+')
print(f'first = {first}')

second = ''
temp = open(file_54_2, 'r')
for i in temp: second += i
second = second.replace(' = 0', '')
second = second.split('+')
print(f'second = {second}')
result = 0
print(f'result = {result}')
final_result = ''
temp_result = []
for i in range(len(first)):
    for j in range(len(second)):         
        member = first[i]
        member = member.replace(' ', '')
        print(f'member = {member}')
        member2 = second[j]
        member2 = member2.replace(' ', '')
        print(f'member2 = {member2}')
        if member[-1] == member2[-1]:
            index1 = member.find('x')
            index2 = member2.find('x')
            number = member[0: index1]
            print(f'number = {number}')
            number2 = member2[0: index2]
            result = int(number) + int(number2)
            result = f'{str(result)}x**{member[-1]}'
            temp_result.append(result)


print(f'result = {result}')
print(f'temp_result = {temp_result}')



# print(first)
# print(second)