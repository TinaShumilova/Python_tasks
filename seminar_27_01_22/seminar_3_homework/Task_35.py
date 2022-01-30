def number_multily_position(first, last):
    temp_list = [first]
    j = 0
    for i in range(first, last):
        temp_list.append(temp_list[j] * (i+1))
        j +=1    
    return temp_list

#print(number_multily_position(1, 5))
