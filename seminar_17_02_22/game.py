from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

import random

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
    
    