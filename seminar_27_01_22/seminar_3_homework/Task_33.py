def Words_count(text1, text2):
    return text1.count(text2)

#print(Words_count(text1 = input(), text2 = input()))

def Simbol_count(text1, text2):
    count = 0
    temp_text2 = [' ']
    k=0
    for i in range(len(text2)):
            if text2[i] != temp_text2[k]:        
                for j in range(len(text1)):
                    if text2[i]== text1[j]:
                        count += 1
                        temp_text2.append(text2[i]) 
                k+=1                      
    return count

print(Simbol_count(text1 = input(), text2 = input()))


