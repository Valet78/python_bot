from login.act import *     # Token bot
import urllib3
from os import getcwd, path
from time import ctime, strptime, strftime
from datetime import datetime as dt
from game import send_bot

def load_exchange(dtime: str) -> str:                # – находит курсы валют и выводит закодированную информацию;
    URL = 'http://www.cbr.ru/scripts/XML_daily.asp?date_req=' + dtime       # '20/12/2022'    
    http = urllib3.PoolManager()    
    resp = http.request('POST', URL)
    res_data = resp.data.decode('windows-1251')
    print(URL)
    return res_data

def get_data_xml(dtime: str) -> list[str, dict[str, dict[str, str]]]:                       # Проверяем актуальность данных файли и загружаем данные
    pathFile = getcwd() + '\\exchnge.xml'
    try:
        with open(pathFile, mode='r', encoding='windows-1251') as file_ex:
            text_file = file_ex.read()
            time_m = path.getmtime(pathFile)        # определяем время модифицации файла
            time_txt = strptime(ctime(time_m))            
            date_now = dt.now()                     # текущее время
            if time_txt.tm_year != date_now.year or \
               time_txt.tm_mon != date_now.month or \
               time_txt.tm_mday != date_now.day:               
                    raise FileNotFoundError           

    except FileNotFoundError:                          # если файл не найден или необходимо обновить
        text_file = load_exchange(dtime)  
        with open(pathFile, mode='w', encoding='windows-1251') as file_ex:
            file_ex.write(text_file)
    ind_date = text_file.find('ValCurs Date') + 14
    date_kurs = text_file[ind_date:  ind_date + 10]
      
    ind = 0
    dict_valut = {}
    root_node = ET.parse(pathFile).getroot()            # получаем "древо" (по сути двумерный массив) 
    for tag in root_node.findall('Valute'):  
        valut_id = tag.attrib['ID'] 
        dict_valut[valut_id] = {'NumCode':root_node[ind][0].text, 'CharCode':root_node[ind][1].text, 
            'Nominal':root_node[ind][2].text, 'Name':root_node[ind][3].text, 'Value':root_node[ind][4].text}
        ind += 1
    
    return date_kurs, dict_valut
""" 
Пример XML файла

<ValCurs Date="24.12.2022" name="Foreign Currency Market">
    <Valute ID="R01010">
        <NumCode>036</NumCode>
        <CharCode>AUD</CharCode>
        <Nominal>1</Nominal>
        <Name>Австралийский доллар</Name>
        <Value>45,8756</Value>
    </Valute>
    <Valute ID="R01090B">
        <NumCode>933</NumCode>
        <CharCode>BYN</CharCode>
        <Nominal>1</Nominal>
        <Name>Белорусский рубль</Name>
        <Value>25,5083</Value>
    </Valute>
...
    <Valute ID="R01235">
        <NumCode>840</NumCode>
        <CharCode>USD</CharCode>
        <Nominal>1</Nominal>
        <Name>Доллар США</Name>
        <Value>68,6760</Value>
    </Valute>
</ValCurs>
 """
    #############################
def exchange_command(message):  
    send_bot(message, 'Введите идентификатор валюты (3 символа), курс которой необходимо узнать. Например:\n\
    \tUSD - Доллар США\n \tEUR - Евро\n \tCNY - Китайский юань или\n \tALL KURS если интересует другая валюта.')
    bot.register_next_step_handler(message, select_kurs) 

def select_kurs(message):
    date_now = str(dt.now().day) + '/' + str(dt.now().month) + '/' + str(dt.now().year)
    date_kurs, dic_valute = get_data_xml(date_now)    
    valuta = [dic_valute[i]['CharCode'] for i in dic_valute]

    if message.text in valuta:
        for ind_v in dic_valute:
            if dic_valute[ind_v]['CharCode'].count(message.text): id_valute = ind_v

        text_out = f"Курс {dic_valute[id_valute]['Name']} на дату {date_kurs} \n \
            {dic_valute[id_valute]['Nominal']} {dic_valute[id_valute]['CharCode']} - {dic_valute[id_valute]['Value']} руб."
        send_bot(message,text_out)
        send_bot(message, 'Желаете ещё (да/нет или yes/no)?')
        bot.register_next_step_handler(message, select_next)
    elif message.text == 'ALL KURS':
        text_out = f"Курс валют на дату {date_kurs} г.: \n"

        for ind_v in dic_valute:
            text_out += f"{dic_valute[ind_v]['Name']}\n\
            {dic_valute[ind_v]['Nominal']} {dic_valute[ind_v]['CharCode']} - {dic_valute[ind_v]['Value']} руб.\n"           
        
        send_bot(message,text_out)   
        send_bot(message, 'Желаете ещё (да/нет или yes/no)?')
        bot.register_next_step_handler(message, select_next)
    else:
        send_bot(message, 'Введены некорректные данные. Попробуеи снова. \n\
        Введите идентификатор валюты (3 символа), курс которой необходимо узнать. Например:\n\
        \tUSD - Доллар США\n \tEUR - Евро\n \tCNY - Китайский юань или\n \tALL KURS если интересует другая валюта.')
        bot.register_next_step_handler(message, select_kurs)
            
def select_next(message):
    match message.text:
        case 'да', 'yes': exchange_command(message)
        case 'нет', 'no': send_bot(message, 'Рад был помочь Вам. Удачи.')
        





""" 

<CharCode>USD</CharCode>
<Name>Доллар США</Name>

<CharCode>EUR</CharCode>
<Name>Евро</Name>

<CharCode>CNY</CharCode>
<Name>Китайских юаней</Name>

<CharCode>AUD</CharCode>
<Name>Австралийский доллар</Name>

<CharCode>AZN</CharCode>
<Name>Азербайджанский манат</Name>

<CharCode>GBP</CharCode>
<Name>Фунт стерлингов Соединенного королевства</Name>

<CharCode>AMD</CharCode>
<Name>Армянских драмов</Name>

<CharCode>BYN</CharCode>
<Name>Белорусский рубль</Name>

<CharCode>BGN</CharCode>
<Name>Болгарский лев</Name>

<CharCode>BRL</CharCode>
<Name>Бразильский реал</Name>

<CharCode>HUF</CharCode>
<Name>Венгерских форинтов</Name>

<CharCode>HKD</CharCode>
<Name>Гонконгских долларов</Name>

<CharCode>DKK</CharCode>
<Name>Датских крон</Name>

<CharCode>INR</CharCode>
<Name>Индийских рупий</Name>

<CharCode>KZT</CharCode>
<Name>Казахстанских тенге</Name>

<CharCode>CAD</CharCode>
<Name>Канадский доллар</Name>

<CharCode>KGS</CharCode>
<Name>Киргизских сомов</Name>


<CharCode>MDL</CharCode>
<Name>Молдавских леев</Name>

<CharCode>NOK</CharCode>
<Name>Норвежских крон</Name>

<CharCode>PLN</CharCode>
<Name>Польский злотый</Name>

<CharCode>RON</CharCode>
<Name>Румынский лей</Name>

<CharCode>XDR</CharCode>
<Name>СДР (специальные права заимствования)</Name>

<CharCode>SGD</CharCode>
<Name>Сингапурский доллар</Name>

<CharCode>TJS</CharCode>
<Name>Таджикских сомони</Name>

<CharCode>TRY</CharCode>
<Name>Турецких лир</Name>

<CharCode>TMT</CharCode>
<Name>Новый туркменский манат</Name>

<CharCode>UZS</CharCode>
<Name>Узбекских сумов</Name>

<CharCode>UAH</CharCode>
<Name>Украинских гривен</Name>

<CharCode>CZK</CharCode>
<Name>Чешских крон</Name>

<CharCode>SEK</CharCode>
<Name>Шведских крон</Name>

<CharCode>CHF</CharCode>
<Name>Швейцарский франк</Name>

<CharCode>ZAR</CharCode>
<Name>Южноафриканских рэндов</Name>

<CharCode>KRW</CharCode>
<Name>Вон Республики Корея</Name>

<CharCode>JPY</CharCode>
<Name>Японских иен</Name>

 """




if __name__=="__main__":
    # load_exchange('01/01/2022')
    get_data_xml('01/11/2022')