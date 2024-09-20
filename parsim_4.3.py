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
    print(download_storage) # тут получаем ответ с соотвтетсвующей html страницей и выводим в консоль

'''далее нужно получить изображение, переходим на сайт, тыкаем на картинку и ищем где скачать должны быть разрешения экрана,
переходим на страницу сайта показать код и ищем image data или там где кнопка скачать картинку
далее преходим к parsim_4.4.py
'''
