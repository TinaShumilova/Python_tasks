from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, ConversationHandler
import datetime
from game import *

def temp(update: Update, context: CallbackContext):
    temp = update.message.text
    item = temp.split()
    print(item)
    number = int(item[0])
    print(number)
    print(type(number))
    #update.message.reply_text(number)
    return number

def help_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'/delete\n/help\n/game\n')

def deleted_command(update: Update, context: CallbackContext):
    str = update.message.text
    print(str)
    tr = str.split()
    print(tr)
    tr.remove(tr[0])
    print(tr)
    [tr.remove(word) for word in tr[:] if 'абв' in word]
    print(tr)
    text = ''.join(tr)
    update.message.reply_text(f'результат = {text}')

def game_command(update: Update, context: CallbackContext):
    sweets_value = update.message.text
    item = sweets_value.split()
    sweets = int(item[1])
    max_sweets = 28
    turn = 1
    def get_sweets(turn):
        while True:
            if turn == 1:
                update.message.reply_text(f'Заберите {get_hint_user(sweets, max_sweets)} конфет')
                update.message.reply_text(f'Сколько конфет забрать игроку {turn}:')
                temp_text = temp(update, context)
                print(type(temp_text))
                sweet_count = int(temp_text)
            else:
                sweet_count = get_hint_comp(sweets, max_sweets)
                update.message.reply_text(f'Бот ввел число: {sweet_count}')
            if sweet_count >= max_sweets:
                sweet_count = max_sweets
            return sweet_count    

    while True:
        update.message.reply_text(f'Конфет осталось {sweets}')
        sweets -= get_sweets(turn)
        if sweets <= 0:
            turn = 'Бот' if turn == 2 else 'Человек'
            update.message.reply_text(f'Победил игрок {turn}')
            break    
        turn = 2 if turn == 1 else 1


