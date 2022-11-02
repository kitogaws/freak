import requests
from bs4 import BeautifulSoup


MAIN_URL = ''
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'


def open_page(url):
    headers = {'User-Agent' : USER_AGENT}
    response = requests.get(url,headers=headers)
    return response.text


def analyze_page_content(content):
    soup = BeautifulSoup(content, 'html')
    return soup


def get_products_cards(soup):
    list_ = soup.find('div', class_ = "catalog")
    product_cards = list_.find_all('span', class_ ="catalog")
    return product_cards


def get_product_info(product_card):
    image_element = product_card.find('div', class_="l_class")
    image_link = image_element.find('img').get("src")
    
    price_element = product_card.find('span', class_="price-localized")
    price = price_element.text
    
    options_element = product_card.find('span', class_="goods-name")
    options = options_element.text
    
    name_element = product_card.find('strong', class_="brand-name")
    name = name_element.text
    
    information = {
    'name' : name.strip('/'),
    'image_link' : image_link,
    'price' : price,
    'options' : options
    }
    return information


def write_to_json(data):
    import json
    with open('products.json', 'w') as file:
        json.dump(data, file)

def write_to_csv(data):
    import csv
    with open('products.csv', 'w') as file:
        fieldnames = ['title', '']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for product in data:
            writer.writerow({})


def main():
    page_count = 1
    all_product_cards = list()
    for page in range(1):
        url = f'{MAIN_URL}?page={page}'
        page_content = open_page(url)
        soup = analyze_page_content(page_content)
        product_cards = get_products_cards(soup)
        all_product_cards.extend(product_cards)
    print(len(all_product_cards))
    total_info = list()
    for product_card in all_product_cards:
        product_info = dict(get_product_info(product_card))
        total_info.append(product_info)
        print(total_info)
# write_to_json(total_info)
# write_to_csv(total_info)
if __name__ == '__main__':
    main()