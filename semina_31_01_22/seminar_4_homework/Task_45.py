num_10 = int(input('Введите чирсло - '))

def find_binary(num_10):
    num_2 = ''
    temp_num = num_10
    while temp_num != 0:
        num_2 += str(temp_num % 2)
        temp_num //= 2
    num_2 = num_2[::-1]
    return num_2

print(find_binary(num_10))
