# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup


def parse(dom):
    soup = BeautifulSoup(dom, 'html.parser')
    links = soup.find(id='main-content').find_all('a')
    img_urls = []
    for link in links:
        if link['href'].startswith('http://i.imgur.com'):
            img_urls.append(link['href'])

    return img_urls