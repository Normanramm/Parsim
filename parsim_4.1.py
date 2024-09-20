import requests
import fake_useragent
from bs4 import BeautifulSoup

storage_number = 1  # номер страницы сайта
link = f"https://www.zastavki.com/rus/Nature/Beach/{storage_number}/"

response = requests.get(link).text
soup = BeautifulSoup(response, 'lxml')
block = soup.find('div',
                  class_='row flex flex-middle flex-flow-row xs-block flex-between')  # получаем блок с картинками
all_image = block.find_all('div',
                           class_='col-sm-4 text-center image-line')  # получаем картинки

# разбить каждую картинку с страницы и искать в блоке div ссылку на страницу картинки ищем href
# for image in all_image:
    # print(image)
    # print('\n\n')

# далее отправляем запрос на получение ссылок на картинки со страниц
for image in all_image:
    image_link = image.find('a').get('href')
    print(image_link)

# после переходим (parsim_4.2.py) там более чистый код и дальнешие действия