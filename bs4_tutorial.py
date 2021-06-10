import requests
from requests.api import get
from requests.models import HTTPError
from bs4 import BeautifulSoup
from pathvalidate import sanitize_filename



def get_title(response):
    soup = BeautifulSoup(response.text, 'lxml')
    title_tag = soup.find('body').find('div', class_='e-title text-center small').text.strip()
    post_text = soup.find('body').find('div', class_='flex subheading font-weight-light pa-3 event-content').text
    date = soup.find('div', class_='text-lg-right article-date').text
    try:
        link_image = soup.find('body').find('div', class_='cover__wrapper').find('img')['src']
    except AttributeError:
        link_image = None
    return title_tag, post_text, link_image, date

if __name__ == "__main__":
    for id in range(120900, 123000):
        url = 'https://ldpr.ru/event/{}'.format(id)
        response = requests.get(url)
        try:
            response.raise_for_status()
            a = get_title(response)
            if a[3] == "сегодня":
                print("Заголовок:", a[0])
                print("Текст:", a[1])
                print("Картинка:", a[2])
                print("id:", id)
        except HTTPError:
            pass
