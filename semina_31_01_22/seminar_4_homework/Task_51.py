#Составить список простых множителей натурального числа N

N = int(input('Введите число - '))

def prime_factors_list(N):
    factors_list = [1]
    temp_num = 2
    while N > 1:
        while N % temp_num == 0:
            factors_list.append(temp_num)
            N /= temp_num
        temp_num += 1
    return factors_list

print(prime_factors_list(N))