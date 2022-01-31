def fibonacci(n):
    if n in [0, 1]: return 1
    if n >0: return fibonacci(n-1) + fibonacci(n-2)
    if n < 0: return fibonacci(n+2) - fibonacci(n+1)

def list_fibonacci(min, max):
    list_fibo = []
    for i in range(min -1, max):
        list_fibo.append(fibonacci(i))
    return list_fibo

print(list_fibonacci(-10, 10))


N = 10
def feb_print(N):
    list_1 = [0]
    feb1 = 1
    feb2 = 0
    for i in range(N):
        feb1, feb2 = feb2, feb1+feb2
        list_1.append(feb2)
        list_1.insert(0,((-1) **(i) * feb2))    
    print(list_1)

feb_print(N)
