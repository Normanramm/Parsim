import requests

'''создаем заранее список прокси серверов
зачем нужны прокси при парсинг сайта ?
В данном случае используем чтобы сайт думал, что это разные пользователи,
это помогает обходить блокировки или выдавать себя за другого человека, так как будут разные IP адреса в запросах
В этой программе можно узнать валидный IP адрес или нет
'''

with open('proxy') as file:
    proxy_base = ''.join(file.readlines()).strip().split('\n')

for proxy in proxy_base:
    proxies = {
        'http': f'http://{proxy}',
        'https': f'http://{proxy}'
    }

    link = "https://icanhazip.com/"
    try:
        response = requests.get(link, proxies=proxies, timeout=2).text
        print(f'IP:{response}')
    except:
        print('Прокси не валидный')



