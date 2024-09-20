import requests
import fake_useragent
from bs4 import BeautifulSoup

# заранее создаем логин и пароль на сайте


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