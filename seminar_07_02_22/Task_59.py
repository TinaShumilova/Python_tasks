sweets = 121
max_sweets = 28
turn = 1
def get_hint_user(sweets, max_sweets):
    if max_sweets >= sweets:
        return sweets
    number = sweets // max_sweets
    y = number * max_sweets + 1
    return sweets - y

def get_hint_comp(sweets, max_sweets):
    if max_sweets >= sweets:
        return sweets
    number = sweets // max_sweets    
    y = number * max_sweets + 1
    if y >= sweets:
        y = (number - 1) * max_sweets + 1
    return (random.randint(1, sweets if max_sweets > sweets else max_sweets) 
    if sweets - y == 0 else sweets - y)

def get_sweets(turn):
    while True:
        if turn == 1:
            print(f'Заберите {get_hint_user(sweets, max_sweets)} конфет')
            sweet_count = int(input(f'Сколько конфет забрать игроку {turn}:'))
        else:
            sweet_count = get_hint_comp(sweets, max_sweets)
            print(f'Бот ввел число: {sweet_count}')
        if sweet_count >= max_sweets:
            sweet_count = max_sweets
        return sweet_count    

while True:
    print(f'Конфет осталось {sweets}')
    sweets -= get_sweets(turn)
    if sweets <= 0:
        turn = 'Бот' if turn == 2 else 'Человек'
        print(f'Победил игрок {turn}')
        break    
    turn = 2 if turn == 1 else 1
