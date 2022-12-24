from login.act import *     # Token bot
from game import *


@bot.message_handler(commands=['start', 'help', 'game_117'])
def send_welcome(message):    
    match message.text:
        case '/start':
            text_out = 'Добро пожаловать, ' + message.from_user.username
            send_bot(message, text_out)
        case '/help':
            text_out = 'В настоящее время Вы можете воспользоваться следующими командами: \n \
                1. /start - запуск бота\n \
                2. /help - собственно вызов этого сообщения\n \
                3. /game_117 - игра с конфетками.'
            send_bot(message, text_out)    
        case '/game_117':  
            bot.register_next_step_handler(message,game_117)          
        #     textov = f'Я, предлагаю Вам сыграть в игру:\n \
        #         В игре у игроков есть кучка, в ней 117 конфет. \n \
        #         Два игрока поочереди достают из кучки конфетки, \n \
        #         но не более 28 конфет за один ход. \n \
        #         Выигрывает тот игрок, чей ход окажется последним. \n \
        #         Он и забирает все конфеты себе.'  
        #     send_bot(message, textov)
        #     send_bot(message, 'Играем да/нет')   
             
            # bot.register_next_step_handler(message, start_game)  

""" Далее код самой игры 
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

"""
##### 
# @bot.message_handler(func=lambda m: True)
# def echo_all_1(message):
#     send_bot = lambda x: bot.send_message(message.chat.id, x)
    
#     send_bot('Next')
    
# @bot.message_handler(func=lambda m: True)
# def echo_game(message):
#     send_bot = lambda x: bot.send_message(message.chat.id, x)
#     send_bot('Next')
bot.infinity_polling()







