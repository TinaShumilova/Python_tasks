def Numbers_sum_in_R(r):
    r = input('Введите любое число - ')
    summa = 0
    for i in range(len(r)):
        if r[i] != '.' and r[i] !=',' and r[i] !='-':
            summa += int(r[i])
    return summa
R= None
#print(Numbers_sum_in_R(R))
