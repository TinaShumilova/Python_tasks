#Определить, позицию второго вхождения строки в списке либо сообщить, что его нет

text1 = '«Текст» — российский криминально-драматический психологический триллер'\
' режиссёра Клима Шипенко[4], тэкранизация романа-бестселлера «Текст» (2017) писателя'\
' Дмитрия Глуховского, который сам адаптировал свой роман в киносценарий[5]. ' #где мы ищем

text2 = 'Текст' # что мы ищем

def position_second_occurrence(text1, text2):
    temp_list = text1.split()
    count = 0
    index = 0
    answer = ''
    for i in range(len(temp_list)):
        if count != 2:
            if text2 in temp_list[i]:
                index = i
                count += 1
        else: break
    if count == 0: answer = f'строки {text2} в списке нет'
    elif count == 1: answer = f'Строка {text2} имеется только в одном варианте'
    else: answer = f'строка {text2} находится на позиции {index}' 
    return answer

print(position_second_occurrence(text1, text2))

