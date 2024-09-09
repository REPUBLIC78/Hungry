import requests
from bs4 import BeautifulSoup 

# get soup
def get_soup(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    return soup

# поиск ссылок
def find_links(url, link_array):
    try:
        soup = get_soup(url)
        links = soup.find_all('a', href=True)
        for i in links:
            link_array.append(i['href'])
        link_array = plus_url(url, link_array)
        link_array = remove_duplicates(link_array)
        link_array = only_forwarding(link_array)
    except:
        pass

# добавляет ссылки из одного урла в другой
def plus_url(url, link_array):
    for i in range(len(link_array)):
        if not link_array[i].startswith('http'):
            link_array[i] = url + link_array[i]
    return link_array

# возвращает только переходящие ссылки
def only_forwarding(link_array):
    for i in link_array:
        if not 'https://ru.wikipedia.org/' in i:
           link_array = link_array.remove(i)  
    return link_array   

# удаляет дубликаты ссылок
def remove_duplicates(link_array):
    link_array = set(link_array)
    return list(set(link_array))
            