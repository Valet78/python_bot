
""" 



def end_prog_game(win_gamer: int):                     # Конец игры и вывод результата принимает номер победителя
    log_win(f'Игра закончена с победой {win_gamer} игрока\n', ValueDate(dt.now()))
    # Up.message.reply_text(f'\nПобедил игрок номер {win_gamer}. Он забирает все конфеты себе.')
    # Up.message.reply_text('\nИ, да, игра окончена!!!\n')
    

def main():
    res = run_prog_game()
    end_prog_game(res)


 """