import requests
import multiprocessing

'''Допустим нужно скачать много картинок или файлов
можно использовать модуль multiprocessing'''

def handler(proxy):

    link = "https://icanhazip.com/"

    proxies = {
        'http': f'http://{proxy}',
        'https': f'http://{proxy}'
    }

    try:
        response = requests.get(link, proxies=proxies, timeout=2).text
        print(f'IP:{response.strip()}')
    except:
        print('Прокси не валидный')

with open('proxy') as file:
    proxy_base = ''.join(file.readlines()).strip().split('\n')

with multiprocessing.Pool(multiprocessing.cpu_count()) as process:
    process.map(handler, proxy_base)


'''В данном коде используется библиотека requests для отправки HTTP-запросов и библиотека multiprocessing для параллельного выполнения задач.
Вначале создается функция handler, которая принимает на вход прокси-адрес и отправляет GET-запрос на ссылку 
'https://icanhazip.com/'. Если запрос успешен, то выводится IP-адрес, полученный от сервера.
Если запрос не успешен, то выводится сообщение 'Прокси не валидный'.
Затем открывается файл 'proxy' и все строки в файле читаются и добавляются в список proxy_base.
Затем создается пул процессов с количеством процессов, равным количеству ядер процессора. 
Этот пул процессов используется для параллельного выполнения функции handler для каждого прокси-адреса в proxy_base.
Код использует метод map для выполнения функции handler для каждого элемента в proxy_base.
Результаты выполнения функции handler выводятся на экран.'''