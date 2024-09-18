import requests
from bs4 import BeautifulSoup

url = 'https://www.playground.ru/lord_of_the_rings_the_battle_for_middle-earth/file/maps'
responce = requests.get(url).text
soup = BeautifulSoup(responce, 'lxml')
block = soup.find('div', id = 'postListContainer')
block_2 = block.find_all('div', 'post-title')
print(block_2)


"""В данном коде мы используем библиотеки requests и BeautifulSoup для парсинга веб-страницы.

1. Вначале мы импортируем необходимые библиотеки.
2. Затем мы устанавливаем URL-адрес страницы, которую мы хотим проанализировать.
3. Далее мы отправляем GET-запрос на эту страницу с помощью модуля requests и сохраняем ответ в переменную responce.
4. Затем мы преобразуем ответ в текст с помощью метода text.
5. Далее мы создаем объект BeautifulSoup, передавая в него ответ и указывая 'lxml' как парсер.
6. Затем мы находим блок на странице с помощью метода find, передавая в него идентификатор 'postListContainer'.
7. Далее мы находим все элементы с классом 'post-title' внутри найденного блока с помощью метода find_all.
8. Наконец, мы выводим найденные элементы с помощью функции print.

Этот код будет выводить список всех заголовков статей на странице, указанной в переменной url.
"""