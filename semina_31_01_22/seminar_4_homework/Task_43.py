# Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д. 
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 

list1 = [2, 3, 5, 6]

def find_pares_multy(list1):
    list2 = []
    last = len(list1) - 1 
    for i in range(0, (last//2) + 1):
        temp = list1[i] * list1[last]
        list2.append(temp)
        last-=1
    return list2

print(f'{list1} => {find_pares_multy(list1)}')

