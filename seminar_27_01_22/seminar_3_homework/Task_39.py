# Реализовать алгоритм задания случайных чисел. 
# Без использования встроенного генератора псевдослучайных чисел

import datetime
from random import shuffle
def find_index():
    list2=[]
    current_date_time = datetime.datetime.now().timestamp()
    number = str(current_date_time)
    [list2.append(int(i)) for i in number if i != '.']
    return list2

def create_start_list(min, max):
    list1 = []
    [list1.append(i) for i in range(min, max +1)]
    #list1 = int(list1)
    return list1

def final_list(count, min, max):
    list3 = []
    list1 = create_start_list(-5, 5)
    print(list1)
    list2 = find_index()
    print(list2)
    for i in range(count):
        for j in range(len(list2)):
            if len(list3) < count:
                if list2[j] <= count:
                    index = list2[j]
                    list3.append(list1[index])
                else: j += 1
    shuffle(list3)
    return list3




print(final_list(10, -5, 5))
