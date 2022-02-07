#52.	Дана последовательность чисел. Получить список неповторяющихся
#  элементов исходной последовательности
#Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

list1 = [1, 2, 3, 5, 1, 5, 3, 10]
list2 = [list1[0]]

#list2.append(list1[0])
for i in list1:
    count = 0
    for j in list2:
        if i == j:
            count +=1
    if count == 0: list2.append(i)
    
           
print(list1)
print(list2)


