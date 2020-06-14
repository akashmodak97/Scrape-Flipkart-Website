# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 20:54:46 2019

@author: AKASH
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
from pandas import DataFrame
urlname = "https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniq"

try:
    page = urlopen(urlname)
except:
    print("Error in opening the page")
soup = BeautifulSoup(page,'html.parser')
print(soup)
products = []
prices = []

for i in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
    name=i.find('div',{'class':'_3wU53n'})
    price=i.find('div',{'class':'_1vC4OE _2rQ-NK'})
    products.append(name.text)
    prices.append(price.text)

df = DataFrame({'Products': products,'Prices':prices})
print(df)
df.to_csv('E:\\filename.csv',index=False,encoding='utf-8')
