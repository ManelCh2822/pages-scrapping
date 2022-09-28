

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

main_list = []

def extract(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 Avast/94.0.12310.62'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup.find_all('div', class_ = 'row businessCapsule--mainRow')

def transform(articles):
    for item in articles:
        name = item.find('span', class_ = 'businessCapsule--name')
        address = item.find('span', {'itemprop': 'address'}).text.strip().replace('\n', '')
        try:
            website = item.find('a', class_ = 'btn btn-yellow businessCapsule--ctaItem')['href']
        except:
            website = ''
        try:
            tel = item.find('span', class_ = 'business--telephoneNumber').text.strip()
        except:
            tel = ''

        business = {
            'name': name,
            'address': address,
            'website': website,
            'tel': tel
        }
        main_list.append(business)
    return

def load():
    df = pd.DataFrame(main_list)
    df.to_csv('coffeeshopYelowPage.csv', index=False)

for x in range(1,9):
    print(f'Getting page {x}')
    articles = extract(f'https://www.yell.com/ucs/UcsSearchAction.do?scrambleSeed=540269558&keywords=cafes+%26+coffee+shops&location=glasgow&pageNum={x}')
    transform(articles)
    time.sleep(5)

load()
print('Saved to CSV')