import requests
import fake_useragent
from bs4 import BeautifulSoup

# заранее создаем логин и пароль на сайте

'''В данном коде используется библиотека requests для отправки HTTP-запросов и библиотека fake_useragent для генерации случайного User-Agent. Также используется библиотека BeautifulSoup для парсинга HTML-страниц.
Вначале создается сессия requests.Session(), которая используется для сохранения cookie. Затем задается ссылка на страницу регистрации, заходим в покажи код, вводим рандомные данные и в network берем эту ссылку.
Далее создается словарь data с данными, которые будут отправлены в запросе. Затем отправляется POST-запрос на ссылку link с данными data и заголовками headers.
После этого создается ссылка на страницу профиля и отправляется GET-запрос на эту ссылку. Результат запроса выводится на экран.
Затем создается словарь cookies_dict, который содержит все cookie из первой сессии. Затем создается вторая сессия requests.Session() и все cookie из первого сессии добавляются во вторую сессию.
Наконец, отправляется GET-запрос на ссылку profile_info с использованием второй сессии и результат запроса выводится на экран.
Код использует метод POST для отправки данных на сервер и метод GET для получения данных с сервера. Также используется метод set для добавления cookie во вторую сессию.'''

# для записи cookie
session = requests.Session()  # для сохранения cookie
# страница регистрации, заходим в покажи код, вводим рандомные данные и в network берем эту ссылку
link = 'https://www.playground.ru/api/security.login'

# далее идем в запрос и ищем данные и создаем словарь {data} с этими данными из запроса

user = fake_useragent.UserAgent().random
headers = {'User-Agent': user}

data = {'password': 'AmbivalentEaston',
        'message': '4J8ReQVZ'
        }

# отправляем запрос
response = session.post(link, data=data, headers=headers).text

# для просмотра профиля
profile_info = 'https://users.playground.ru/5370291/'
profile_response = session.get(profile_info, headers=headers).text
# print(profile_response)

# для того чтобы каждый раз не авторизовываться в аккаунте, можно сохранить cookie и их подгружать
# список значений cookies
cookies_dict = [
    {"domain": key.domain, "name": key.name, "path": key.path, "value": key.value}
    for key in session.cookies
]
# из первой сессии записали во вторую сессию куки
session2 = requests.Session()

# пробегаемся по всем cookies
for cookie in cookies_dict:
    session2.cookies.set(**cookie)

resp = session2.get(profile_info, headers=headers)
print(resp.text)
