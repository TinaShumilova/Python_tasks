tex = '«Текст» — российский криминально-драматический психологический триллер'\
' режиссёра Клима Шипенко[4], экранизация романа-бестселлера «Текст» (2017) писателя'\
' Дмитрия Глуховского, который сам адаптировал свой роман в киносценарий[5]. '

list1 = tex.split()

def find_number_in_list(number, list1):
    result = ''
    for i in list1:
        if str(number) in i: 
            result = f'число {number} присутствует в заданном списке строк'
            break
        else: result = 'нет'
    return result

print(find_number_in_list(8, list1))

               
        
