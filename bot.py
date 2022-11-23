import telebot
import requests
import csv
from bs4 import BeautifulSoup

TOKEN = '5962237352:AAEEoNhO420WAV_XWgGdSNJqzItaLRcFo-w'
bot = telebot.TeleBot(TOKEN)
keyword = telebot.types.ReplyKeyboardMarkup()
button1 = telebot.types.KeyboardButton(1)
button2 = telebot.types.KeyboardButton(2)
button3 = telebot.types.KeyboardButton(3)
button4 = telebot.types.KeyboardButton(4)
button5 = telebot.types.KeyboardButton(5)
button6 = telebot.types.KeyboardButton(6)
button7 = telebot.types.KeyboardButton(7)
button8 = telebot.types.KeyboardButton(8)
button9 = telebot.types.KeyboardButton(9)
button10 = telebot.types.KeyboardButton(10)
button11 = telebot.types.KeyboardButton(11)
button12 = telebot.types.KeyboardButton(12)
button13 = telebot.types.KeyboardButton(13)
button14 = telebot.types.KeyboardButton(14)
button15 = telebot.types.KeyboardButton(15)
button16 = telebot.types.KeyboardButton(16)
button17 = telebot.types.KeyboardButton(17)
button18 = telebot.types.KeyboardButton(18)
button19 = telebot.types.KeyboardButton(19)
button20 = telebot.types.KeyboardButton(20)
button21 = telebot.types.KeyboardButton('quit')
button22 = telebot.types.KeyboardButton('link')
button23 = telebot.types.KeyboardButton('title')
keyword.add(button1, button2, button3, button4, button5, button6, button7,
             button8, button9, button10, button11, button12, button13, button14,
             button15, button16, button17, button18, button19, button20, button21, button23, button22)



url = f'https://kaktus.media/?lable=8&date=2022-11-23&order=time'
html = requests.get(url).text
soup = BeautifulSoup(html, 'lxml')
news = soup.find_all('div', class_='ArticleItem')[:20]

@bot.message_handler(commands=['start', 'news', 'link', 'title', 'quit'])
def start(message):
    for i in range(len(news)):
        bot.send_message(message.chat.id, f'{i+1})   {news[i].text.strip()}', reply_markup=keyword)
    bot.register_next_step_handler(message, check)

def check(message):
    if message.text.isdecimal():
        link = news[int(message.text)-1].find('a', class_='ArticleItem--image').get('href')
        bot.send_message(message.chat.id, f'{link}')
    elif message.text == 'quit':
        bot.send_message(message.chat.id, 'Goodbye')
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEGhG9jfft-NZ13hOYDak7ei2uQxb3_pgACdRoAAit28UgjpZ_QxwlC7ysE')


bot.polling()





# def write_to_csv(data):
#     with open('news.csv', 'a') as file:
#         writer = csv.writer(file)
#         writer.writerow([data['title'], data['link']])

# def get_html(url_):
#     response = requests.get(url_)
#     # print(response.status_code) 
#     html = response.text
#     return html

# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     news = soup.find('div', class_ ='Tag--articles').find_all('div', class_= 'Tag--article')
#     # print(news)
#     score = 0
#     for i in news:
#         try:
#             title = i.find('div', class_= 'ArticleItem--data ArticleItem--data--withImage').find('a', class_ = 'ArticleItem--name').text.strip()
#         except:
#             title = 'Нет актаульных новостей'

#         try:
#             link = i.find('a', class_ = 'ArticleItem--name').get('href')
#         except:
#             link = 'Нет актуальных фото'           
#         data = {
#             'title': title, 
#             'link':link, 
#             }
#         write_to_csv(data)
#         score +=1
#         if score==20:
#             break

# def main():

#     url_ = 'https://kaktus.media/?lable=8&date=2022-11-23&order=time'
#     html = get_html(url_)
#     data =get_data(html)
    
            

# main()