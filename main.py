from login.act import *     # Token bot
from game import send_bot, game_117
from kursi import *

def kurs_topic():
    

    ff=90



@bot.message_handler(commands=['start', 'help', 'game_117', 'kurs'])
def send_welcome(message):  
    match message.text:
        case '/start':
            text_out = 'Добро пожаловать, ' + message.from_user.username
            send_bot(message, text_out)
        case '/help':
            text_out = 'В настоящее время Вы можете воспользоваться следующими командами: \n \
                1. /start - запуск бота\n \
                2. /help - собственно вызов этого сообщения\n \
                3. /kurs - курс валют \n \
                4. /game_117 - игра с конфетками \n'
            send_bot(message, text_out)    
        case '/game_117':             
            game_117(message)    
        case '/kurs':
            send_bot(message, load_exchange())
            # bot.register_next_step_handler(message,kurs_topic)
                 
        

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    # send_bot = lambda x: bot.send_message(message.chat.id, x)
    
    send_bot(message,'Для ознакомления с функциями бота наберите /help')











bot.infinity_polling()







