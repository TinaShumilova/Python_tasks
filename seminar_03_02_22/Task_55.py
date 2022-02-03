#55.	В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1].
# Найти его.

file_numbers = 'seminar_03_02_22/file.txt'
# with open(file_numbers, 'w') as data_text:
#     data_text.writelines(input())

with open(file_numbers) as fn:
        data = fn.readlines()
    
list1 = [int(i) for i in data if i != ' ']
print(list1)

# def number(x):
#     return x-1
# for i in range(len(list1)-1, -1, -1):
#     if list1[i] - 1  != list1[i-1]:
#         print(list1[i] - 1)
#         break 

temp_num = [list1[i] for i in range(len(list1)-1, -1, -1) \
    if list1[i] - 1  != list1[i-1]]
print(temp_num)
num = lambda x: x-1
print(num(temp_num[0]))