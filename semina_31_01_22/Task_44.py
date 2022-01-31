list2 = [1.3, 1.8, 1.9, 1.2, 3.1]

def find_drob(list2):
    list3 = []
    for i in list2:
        list3.append(round(i%1, 2))
    return list3

def find_max(list3):
    max = list3[0]
    for i in range(len(list3)):
        if list3[i] > max: max = list3[i]
    return max
def find_min(list3):
    min = list3[0]
    for i in range(len(list3)):
        if list3[i] < min: min = list3[i]
    return min

def raznostj(list2):
    list3 = find_drob(list2)
    maxi = find_max(list3)
    mini = find_min(list3)
    return maxi - mini 

print(raznostj(list2)) 



