import requests
from bs4 import BeautifulSoup
import csv




def write_to_csv(data):
    with open('task2.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([data['title'], data['img'], data['price'], data['description']])

def get_html(url_):
    response = requests.get(url_)
    # print(response.status_code) Можно запустить для начала
    html = response.text
    return html

def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    page_list = int(soup.find('ul', class_ = 'pagination').find_all('li')[-1].find('a').get('data-page'))
    # print(page_list) Это для меня
    return page_list


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    cars = soup.find('div', class_ = 'search-results-table').find_all('div', class_ ='list-item list-label')
    # print(cars)
    for i in cars:
        try:
            title = i.find('div', class_ = 'block title').find('h2', class_='name').text.strip()
        except:
            title = ''

        try:
            price = i.find('div', class_ = 'block price').find('strong').text
        except:
            price = ''

        try:
            img = i.find('img').get('data-src')
        except:
            img = ''
            
        try:
            description = ' '.join(i.find('div', class_ = 'block info-wrapper item-info-wrapper').text.split())
        except:
            description = ''
             
        data = {
            'title': title, 
            'img':img, 
            'price':price,
            'description':description
            }
        write_to_csv(data)


def main():

    url_ = 'https://www.mashina.kg/search/all/'
    html = get_html(url_)
    # data =get_data(html)
    page = 1
    number = int(get_total_pages(html))
    comm = '?page='
    while page <= number:
        print(page)
        url_ = f'https://www.mashina.kg/search/all/{comm}{page}'
        html = get_html(url_)
        number = int(get_total_pages(html))
        get_data(html)
        page +=1 

with open('task2.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['title', 'price', 'img', 'description'])
            

main()