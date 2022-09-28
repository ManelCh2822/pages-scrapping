# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 20:17:56 2021

@author: Fujitsu
"""

import requests
from bs4 import BeautifulSoup


url="https://www.yell.com/ucs/UcsSearchAction.do?keywords=coffee&location=London&scrambleSeed=843665584&pageNum=1"
header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 Avast/94.0.12310.62"}
r=requests.get(url,headers=header)
soup = BeautifulSoup(r.content,'html.parser')

print(soup.title)  #  to see if  everything is working

article = soup.find_all('div', class_ = 'row businessCapsule--mainRow')

print(len(article))
print(article[0])

for item in article:
    name = item.find('span', class_ = 'businessCapsule--name')
    link = item.find('a', class_ = 'businessCapsule--title')['href']
    address = item.find('span', {'itemprop': 'address'}).text.strip().replace('\n','')
    try:
        website = item.find('a', class_ = 'btn btn-yellow businessCapsule--ctaItem')['href']
    except:
        website = ''
    try:
        tel = item.find('span', {'class': 'business--telephoneNumber'}).text
    except:
        tel = ''
    try:
        rating = item.find('span', class_ = 'starRating--average').text
        reviews = item.find('span', class_ = 'starRating--total').text
    except:
        rating = ''
        reviews = ''
    business = {
        'name': name,
        'link': 'https://www.yell.com/' + link,
        'address': address,
        'website': website,
        'tel': tel,
        'rating': rating,
        'reviews': reviews,
    }
    print(business)
    
    