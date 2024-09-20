import requests
import fake_useragent
from bs4 import BeautifulSoup

storage_number = 1  # номер страницы сайта
link = f"https://www.zastavki.com" # тут убрали значения, чтобы вело на прямую на сайт

response = requests.get(f'{link}/{storage_number}').text # тут отправляем запрос на ссылку и в этом запросе дописывать значение с страницы
soup = BeautifulSoup(response, 'lxml')
block = soup.find('div',
                  class_='row flex flex-middle flex-flow-row xs-block flex-between')  # получаем блок с картинками
all_image = block.find_all('div',
                           class_='col-sm-4 text-center image-line')  # получаем картинки

# далее отправляем запрос на получение ссылок на картинки со страниц
for image in all_image:
    image_link = image.find('a').get('href')
    download_storage = requests.get(f'{link}{image_link}').text
    download_soup = BeautifulSoup(download_storage, 'lxml') # вставляем новое значение страницы
    # получаем блок с картинкой и в этом блоке ищем class с <a href там где сслыка на скачивание
    download_block = download_soup.find('div',class_='row m-t-10').find('div',class_='row-fluid')
    result_link = download_block.find('a').get('href')
    print(result_link) # получили ссылки на картинки

# далее преходим в parsim_4.5.py там как скачать картинку с сайта

