from login.act import *     # Token bot
from random import randint
from datetime import datetime as dt
from os import getcwd
from csv import *


def game_117(message):            
    textov = f'Я, предлагаю Вам сыграть в игру:\n \
        В игре у игроков есть кучка, в ней 117 конфет. \n \
        Два игрока поочереди достают из кучки конфетки, \n \
        но не более 28 конфет за один ход. \n \
        Выигрывает тот игрок, чей ход окажется последним. \n \
        Он и забирает все конфеты себе.'  
    bot.send_bot(message, textov)
    bot.send_bot(message, 'Играем да/нет')  
    bot.register_next_step_handler(message, start_game)   

def start_game(message) -> str:
    # send_bot = lambda x: bot.send_message(message.chat.id, x)
    if message.text == 'да':    
        log_win('Начало игры', ValueDate())
        textov = f'Отлично! Сейчас мы определимся, кто будет ходить первым. \n \
                Игрок 1 - это собственно Вы сами \n \
                Игрок 2 - это я, бот Firsttest_bot.'    
        send_bot(message, textov)
        gamer = cur_gamer(0)
        send_bot(message, f'Итак, первым ходит Игрок {gamer}')
        run_game(gamer)
        # bot.register_next_step_handler(message, choose_game) 
        msg = ''
    else:  
        send_bot(message, "Ну, и ладно!!!")
    
def send_bot(message, in_text:str):
    bot.send_message(message.chat.id, in_text)

             

def log_win(strMassage: str, strTime: str):
    pathFile = getcwd() + '\\log.csv'
    names = ['Событие', 'Время']
    try:
        with open(pathFile, mode = 'a', encoding='utf-8', newline='\r') as file:
            file_writer = DictWriter(file, lineterminator="\r", fieldnames=names)
            file_writer.writerow({'Событие': strMassage, 'Время':strTime})
    except FileNotFoundError:       
        with open(pathFile, mode = 'w', encoding='utf-8', newline='\r') as file:    
            file_writer = DictWriter(file, lineterminator="\r", fieldnames=names)
            file_writer.writeheader()
            file_writer.writerow({'Событие': strMassage, 'Время':strTime})

def ValueDate() -> str:
    time = dt.now()   
    res_day = [str(time.day), str(time.month), str(time.year)]
    res_time = [str(time.hour), str(time.minute), str(time.second)]
    return (".".join(res_day) + ' г. ' + ':'.join(res_time))


def cur_gamer(tg: int) -> int:          # Выбор первого хода
    match tg:
        case 0: return randint(1, 2)
        case 1: return 2
        case 2: return 1
    

    
def run_game(current_gamer: int) -> int:
    one_candy, two_candy = 0, 0   # количество конфет у игроков
    num_candy = 117

"""    
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

  
def step_bot(num_candy: int) -> int:
    resBot = lambda x: x if x <= 28 else randint(1, 28)
    min_candy = resBot(num_candy)
    Up.message.reply_text(f'Второй игрок (бот) забрал {min_candy} из {num_candy}')
    return min_candy
    
    """