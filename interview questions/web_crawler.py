__author__ = 'Gaurav'

import requests
from bs4 import BeautifulSoup

def basic_crawler(max_pages):
    page = 1
    while page <= max_pages:
        url = "https://www.thenewboston.com/search.php?type=0&sort=reputation&page=" + str(page)
        source_code = requests.get(url)
        simple_text = source_code.text
        soup = BeautifulSoup(simple_text)
        for link in soup.find_all('a', {'class': 'desc-title'}):
            href = "https://www.thenewboston.com" + link.get('href')
            text = link.string
            get_data_for_users(href)
            print href + ":" + text
        page += 1

def get_data_for_users(user_url):
    source_code = requests.get(user_url)
    plain_text = source_code.text
    soup_new = BeautifulSoup(plain_text)
    for item in soup_new.find_all('a', {'class':'titles'}):
        print item.string

def main():
    basic_crawler(5)
    print "Done"

if __name__ == '__main__':
    main()
