#import random
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# random.shuffle(list1)
# print(list1)

from random import randint
# def shake(list1, a, b):
count = len(list1)//2
while count >= 0:
    count1 = randint(0, len(list1)-1)
    temp = list1[count1]
    list1.pop(count1)
    list1.append(temp)
    count -= 1
print(list1)
    

