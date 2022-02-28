#Даны два файла в каждом из которых находится запись многочлена. 
# Сформировать файл содержащий сумму многочленов.
from Task_53 import mnogochlen_2

a = 4
b = 5
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

print(first)