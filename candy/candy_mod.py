# Здесь игровой процесс
from telegram import Update as Up
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from random import randint
""" 
def run_game(type_game: int, current_gamer: int) -> int:
    one_candy, two_candy = 0, 0   # количество конфет у игроков
    num_candy = 117
    while num_candy != 0:
        text_mess = 'Ход первого игрока. ' if current_gamer == 1 else 'Ход второго игрока. '
        Up.message.reply_text(text_mess, end = '')
        minus_candy = step_bot(num_candy) if type_game == 2 and current_gamer == 2 else step_hum(num_candy)
        step_game = lambda x, y: True if y <= 28 and y <= x else False
        num_game = lambda x: 1 if x == 2 else 2
        if step_game(num_candy, minus_candy): 
            num_candy -= minus_candy
            if current_gamer == 1: one_candy += minus_candy
            else: two_candy += minus_candy 
            current_gamer = num_game(current_gamer)
        else: Up.update.message.reply_text('Вы можете одновременно забрать 28 конфет и не более оставшихся.')
    
    return num_game(current_gamer)





def step_hum(num_candy: int) -> int:
    try:
        min_candy = int(Up.message.text(f'Сколько конфет Вы заберёте из {num_candy}? - '))
        return min_candy
    except ValueError:
        Up.message.reply_text('Введены некорректные данные. Ещё разок.')
        step_hum(num_candy)

 """