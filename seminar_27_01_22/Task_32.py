def posledovateljnostj(k):
    return 3*k+1

def number(N):
    dictionary = {} 
    for i in range(1, N+1): 
        dictionary[i] = posledovateljnostj(i)
    return dictionary
            
print(number(int(input('Введите конечное число - '))))