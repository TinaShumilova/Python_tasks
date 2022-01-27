def list_with_posledovateljnostj(n):
    summ = [((1 + 1/i)**i) for i in range(1, n + 1)]
    return sum(summ)

print(list_with_posledovateljnostj(5))
