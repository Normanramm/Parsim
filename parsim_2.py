import requests
from bs4 import BeautifulSoup

url = 'https://www.playground.ru/lord_of_the_rings_the_battle_for_middle-earth/file/maps'
responce = requests.get(url).text
soup = BeautifulSoup(responce, 'lxml')
block = soup.find('div', id='postListContainer')
block_2 = block.find_all('div', 'post-title')
block_3 = block.find_all('div', 'post-metadata')

for i in range(len(block_2)):  # выводим название карт с сайта
    name = block_2[i].text
    print(name)

with open('maps.txt', 'w') as f:  # для сохранения в файл названия карт
    for i in range(len(block_2)):
        name = block_2[i].text
        f.write(name + '\n')

for j in range(len(block_3)):  # выводим время создания карты
    name_2 = block_3[j].text
    print(name_2)

# name = block_2[1].text # выводим название карт с сайта по индексу
# print(name)
