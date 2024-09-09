import requests
from bs4 import BeautifulSoup 

# scraping страницы 
def scrape_url(url):
    response = requests.get(url)
    print(BeautifulSoup(response.text, 'html'))

# response status code
def response_status(url):
    response = requests.get(url)
    print(response)

# парсинг курсов валют
def money_courses():
    url = "https://www.banki.ru/products/currency/cb/"
    soup = get_soup(url)
    courses_money = soup.find_all(class_="Panel__sc-1g68tnu-1 hRExxV currencyCbListItemstyled__StyledPanel-sc-12ajhcx-0 dhonLt")
    for i in courses_money:
        print(i.text)
        
# поиск ссылок
def find_links(url):
    soup = get_soup(url)
    links = soup.find_all('a', href=True)
    for link in links:
        print(link['href'])

# get soup
def get_soup(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    return soup

    