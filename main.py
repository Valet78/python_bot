from login.act import *     # Token bot
from game import send_bot, game_117


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
            # bot.register_next_step_handler(message,game_117)
            game_117(message)         
        
 
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    send_bot = lambda x: bot.send_message(message.chat.id, x)
    
    send_bot('Для ознакомления с функциями бота наберите /help')    

bot.infinity_polling()







