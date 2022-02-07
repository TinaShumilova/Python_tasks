text = 'qwwweeqrrtyyyy'
text2 = ''
text3 = ''
count = 1
for i in range(0, len(text)-1):
    if text[i] == text[i+1]:
        count +=1
        text2 = str(count) + text[i] 
    else: 
        text2 = str(count) + text[i] 
        count = 1
        text3 += text2
text3 += text2

print(text3)    