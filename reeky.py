import time
import requests

from bs4 import BeautifulSoup as bs4 

URL = 'https://akipress.com/allnews/'

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
HEADERS = {'User-agent': USER_AGENT,
'cookie': 'ig_did=F1E696C0-F944-4F79-868E-A5F20427BF99; ig_nrcb=1; mid=Y01W1gALAAGkKX6cVeOQ3ReRPUZ6; csrftoken=GnXY6yKhmC6qajbWt2KTy3I2vZVrqpAj; sessionid=7076063769%3A2K7tIynpktYQOt%3A24%3AAYd5m9W8FTo6_ZjEELPaUajeflqu50IBEFHehcVlnA; ds_user_id=7076063769; shbid="12284\0547076063769\0541697548911:01f722825682526b7739229b885590cef89425437adf03028a799ad5274760d974085f3a"; shbts="1666012911\0547076063769\0541697548911:01f7601a1c8af148028bca8ace9fd19cf8cde371c2db9d8752fe1a73d0627d70f5dd9ed5"; dpr=1.5; datr=71ZNY0e0rz4wiauZGviL7L5i; rur="ODN\0547076063769\0541697548992:01f7c2c50f83b14b16f1b59ad78254f65c4341f9113d920a4680342d47071b45e832d1e2"',
'x-csrftoken': 'GnXY6yKhmC6qajbWt2KTy3I2vZVrqpAj'
}


def benchmark(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f'скорость: {end_time - start_time}')
    return wrapper

@benchmark
def get_response():
    url = 'https://i.instagram.com/api/v1/web/likes/2944562245586156888/like/'
    response_list = []
    for i in range(5):
        response = requests.post(URL, headers=HEADERS)
        print(response)
        response_list.append(response)
        time.sleep(1)
    return response_list

print(get_response())


def get_soup(html, tag, tag_class):
    soup = bs4(html, 'html.parser')
    result = soup.find_all(tag, class_=tag_class)
    return result


def get_result(soup):
    for item in soup:
        print(item.text)


# if __name__ == '__main__':
#     html = get_response(URL, HEADERS)
#     soup = get_soup(html, 'a', 'newstitle')
#     get_result(soup)
