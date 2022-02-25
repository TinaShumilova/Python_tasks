#Строка содержит набор чисел. Показать большее и меньшее число
text = '1542687954236042'

def find_max_symbol_in_string(text):
    maxi = int(text[0])
    min = int(text[0])
    #[maxi = int(text[i]) for i in range(len(text)) (if int(text[i]) > maxi)]
    for i in range(len(text)):
        if int(text[i]) > maxi: maxi = int(text[i])
    for i in range(len(text)):
        if int(text[i]) < min: min = int(text[i])
    return maxi, min

print(find_max_symbol_in_string(text))

text_2 = '15 254 95 1 236 555 458 87'

def find_max_symbol_in_string_2(text_2):
    list1 = list(map(int, text_2.split()))
    maxim = list1[0]
    mini = list1[0]
    for i in range(len(list1)):
        if list1[i] > maxim:
            maxim = list1[i]
    for i in range(len(list1)):
        if list1[i] < mini:
            mini = list1[i]
    return maxim, mini

print(find_max_symbol_in_string_2(text_2))