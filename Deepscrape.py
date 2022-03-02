from bs4 import BeautifulSoup
import requests
import json

output = 'Scraped_file'+'.json'
result = []

url = 'https://www.snapdeal.com/products/books?sort=plrty&SRPID=customsearch&keywd=books'
file = requests.get(url)
data = file.text
soup = BeautifulSoup(data, 'html.parser')


titles = soup.find_all('p', {'class' : 'product-title'})
title = []
for t in titles:
    title.append(t.text)
result.append({'titles':title})

authors = soup.find_all('p', {'class' : 'product-author-name'})
author = []
for i in authors:
    author.append(i.text)
result.append({'authors': author})    

prices = soup.find_all('span', {'class' : 'lfloat product-price'})
price = []
for i in prices:
    price.append(i.text)
result.append({'prices' : price})

print(result)