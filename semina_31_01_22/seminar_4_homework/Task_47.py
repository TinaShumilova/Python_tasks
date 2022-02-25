#Строка содержит набор чисел. Показать большее и меньшее число
# text = '154268795423642'

# def find_max_symbol_in_string(text):
#     maxi = int(text[0])
#     #[maxi = int(text[i]) for i in range(len(text)) (if int(text[i]) > maxi)]
#     for i in range(len(text)):
#         if int(text[i]) > maxi: maxi = int(text[i])
#     return maxi

# print(find_max_symbol_in_string(text))

text_2 = '15 254 95 1 236 555 458 87'

def find_max_symbol_in_string_2(text_2):
    list1 = list(map(int, text_2.split()))
    maxim = list1[0]
    for i in range(len(list1)):
        if list1[i] > maxim:
            maxim = list1[i]
    return maxim

print(find_max_symbol_in_string_2(text_2))