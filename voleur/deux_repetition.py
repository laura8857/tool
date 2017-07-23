# -*- coding: utf-8 -*-
import requests
import bs4

tag = input("請輸入定位元素，class前面加上.，id前面加上# ")
res = requests.get('http://pala.tw/class-id-example/')
soup = bs4.BeautifulSoup(res.text, "lxml")

for drink in soup.select('{}'.format(tag)):
    print(drink.get_text())