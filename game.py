from login.act import *     # Token bot
from random import randint
from datetime import datetime as dt
from os import getcwd, path
from csv import *

current_gamer, all_candy, one_candy, two_candy = 0, 0, 0, 0


def game_117(message):
    textov = f'Я, предлагаю Вам сыграть в игру:\n \
        В игре у игроков есть кучка, в ней 117 конфет. \n \
        Два игрока поочереди достают из кучки конфетки, \n \
        но не более 28 конфет за один ход. \n \
        Выигрывает тот игрок, чей ход окажется последним. \n \
        Он и забирает все конфеты себе.'  
    send_bot(message, textov)
    send_bot(message, 'Играем да/нет')  
    bot.register_next_step_handler(message, start_game)   


def start_game(message): 
    global current_gamer, all_candy    
    if message.text == 'да':    
        log_win('Начало игры', ValueDate())
        textov = f'Отлично! Сейчас мы определимся, кто будет ходить первым. \n \
                Игрок 1 - это собственно Вы сами \n \
                Игрок 2 - это я, бот Firsttest_bot.'    
        send_bot(message, textov)        
        current_gamer = cur_gamer(0)
        all_candy = 117
        send_bot(message, f'Итак, первым ходит Игрок {current_gamer}')      
        run_game(message)       
    else:  
        send_bot(message, "Ну, и ладно!!!")
    


# Основной блок игры
def run_game(message):
    global current_gamer, all_candy, one_candy, two_candy       
    if all_candy != 0:
        if current_gamer == 2:      # Ход бота
            resBot = lambda x: x if x <= 28 else randint(1, 28)
            minus_candy = resBot(all_candy)
            all_candy -= minus_candy
            two_candy += minus_candy
            current_gamer = cur_gamer(current_gamer)         
            if all_candy == 0: 
                send_bot(message,'Ой! Кажется, я забрал последние конфеты.')
                final_game(message)
            else:
                send_bot(message, f'Я (бот) забрал {minus_candy} конфет(ы). \n И теперь у меня {two_candy} конфет(ы), а в куче осталось {all_candy}.')
                # Переход к первому игроку
                send_bot(message, f'В куче {all_candy} конфет(ы). Сколько заберёте Вы?')
                bot.register_next_step_handler(message, step_gamer)
        if current_gamer == 1 and all_candy == 117:      # Ход  игрока
            send_bot(message, f'В куче {all_candy} конфет(ы). Сколько заберёте Вы?')
            bot.register_next_step_handler(message, step_gamer) 
    
# Финал игры
def  final_game(message):   
        global current_gamer, all_candy, one_candy, two_candy
        current_gamer = cur_gamer(current_gamer)
        win_gamer = message.from_user.username if current_gamer == 1 else 'Firsttest_bot'
        textov = f'Итак, игра закончилась победой {win_gamer}. \n Станент скучно, набирай /game_117, сыграем тогда снова.'
        send_bot(message, textov)
        current_gamer, all_candy, one_candy, two_candy = 0, 117, 0, 0
        log_win(f'Конец игры. Победил {win_gamer}.', ValueDate())

# Ход игрока
def step_gamer(message): 
    global current_gamer, all_candy, one_candy, two_candy      
    minus_candy = int(message.text)
    if minus_candy > 0 and minus_candy < 29:    
        one_candy += minus_candy
        all_candy -= minus_candy     
        current_gamer = cur_gamer(current_gamer)
        if all_candy == 0: final_game(message)   
        else:
            send_bot(message, f'В куче остаётся {all_candy} конфет(ы). \n У Вас теперь {one_candy}. Ход второго игрока.')        
            run_game(message)
    else:
        send_bot(message, f'Вы, наверное, ввели неверное значение. \nВы можете забрать от 1 до 28 конфет за ход.\n \
            В куче {all_candy} конфет(ы). Сколько заберёте Вы?')
        bot.register_next_step_handler(message, step_gamer)
    

# Отправка сообщений в чат
def send_bot(message, in_text:str):    
    id_chat = message.chat.id
    bot.send_message(id_chat, in_text)

# Запись событий в файл
def log_win(strMassage: str, strTime: str):
    pathFile = getcwd() + '\\log.csv'
    fil_exist = path.exists(pathFile)
    names = ['Время', 'Событие']
    with open(pathFile, mode = 'a', encoding='utf-8', newline='\r') as file_csv:         
        file_writer = DictWriter(file_csv, lineterminator="\r", fieldnames=names)
        if  not fil_exist: file_writer.writeheader()         # Если файла не существовало  
        file_writer.writerow({'Время':strTime, 'Событие': strMassage})
        

# Формирование текущей даты и времени для файла
def ValueDate() -> str:
    time = dt.now()   
    res_day = [str(time.day), str(time.month), str(time.year)]
    res_time = [str(time.hour), str(time.minute), str(time.second)]
    return (".".join(res_day) + 'г. ' + ':'.join(res_time))

# Перебор текущего игрока и выбор игрока для первого хода
def cur_gamer(tg: int) -> int:          
    match tg:
        case 0: return randint(1, 2)
        case 1: return 2
        case 2: return 1
    

    
if __name__ == '__main__':
    log_win('Test', ValueDate())