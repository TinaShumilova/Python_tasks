def Variety_N(n):
    variety = []
    for i in range(n):
        temp = (-3)**i
        variety.append(temp)
    
    return variety

#print(Variety_N(5))