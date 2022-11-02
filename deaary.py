import requests
from bs4 import BeautifulSoup as b


URL = 'https://www.mashina.kg/search/bmw/all/?color_multiple=4&currency=2&sort_by=price+asc&time_created=all&page=1'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 OPR/91.0.4516.77'
HEADERS = {'User_agent': USER_AGENT}

response = requests.get(URL, headers=HEADERS).text
soup = b(response, 'html.parser')
for i in range(1, 9):
    URL = f'https://www.mashina.kg/search/bmw/all/?color_multiple=4&currency=2&sort_by=price+asc&time_created=all&page={i}'
    response = requests.get(URL)
    soup = b(response.text, 'html.parser')
    price_d = soup.find_all('strong')
    for item in price_d:
        print('Цена:' + item.text)


    car_name = soup.find_all('h2', class_='name')
    for cars in car_name:
        print('Модель машины: ' + cars.text)

    all_views = soup.find_all('div', class_='listing-icons views')
    for view in all_views:
        print('Количество просмотров: ' + view.text)