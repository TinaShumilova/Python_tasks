list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def Sum_noteven_number(list1):
    summa = 0
    for i, number in enumerate(list1):
        if i %2 != 0:
            summa += number
    return summa

print(Sum_noteven_number(list1))