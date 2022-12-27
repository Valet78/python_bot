from login.act import *     # Token bot
import urllib3
from os import getcwd, path
from time import ctime, strptime, strftime
from datetime import datetime as dt


def load_exchange(dtime: str) -> str:                # – находит курсы валют и выводит закодированную информацию;
    URL = 'http://www.cbr.ru/scripts/XML_daily.asp?date_req=' + dtime       # '20/12/2022'    
    http = urllib3.PoolManager()    
    resp = http.request('POST', URL)
    res_data = resp.data.decode('windows-1251')
    return res_data

def get_data_xml(dtime: str) -> dict[str, dict[str, str]]:                       # Проверяем актуальность данных файли и загружаем данные
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
    
    ind = 0
    dict_valut = {}
    root_node = ET.parse(pathFile).getroot()            # получаем "древо" (по сути двумерный массив) 
    for tag in root_node.findall('Valute'):  
        valut_id = tag.attrib['ID'] 
        dict_valut[valut_id] = {'NumCode':root_node[ind][0].text, 'CharCode':root_node[ind][1].text, 
            'Nominal':root_node[ind][2].text, 'Name':root_node[ind][3].text, 'Value':root_node[ind][4].text}
        ind += 1
    
    return dict_valut
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
    
    
    
    # start = text_file.find('ValCurs') + 14      
    # date_kurs = text_file[start: len(text_file)]#: start + 24]


    # print(date_kurs[:10])












if __name__=="__main__":
    # load_exchange('01/01/2022')
    get_data_xml('01/11/2022')