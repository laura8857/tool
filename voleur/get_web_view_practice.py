# -*- coding: utf-8 -*-
import json
import urllib
from urllib.request import urlopen
import requests
import time
from bs4 import BeautifulSoup
import re
import os



WEB_URL = 'https://theinitium.com'


def get_web_page(url):
    time.sleep(0.5)
    resp = requests.get(
        url=url,
    )

    if resp.status_code != 200:
        print('Invalid url:', resp.url)
        return None
    else:
        return resp.text


def get_articles(dom,region):
    soup = BeautifulSoup(dom, 'html.parser')

    # 取得下一頁的連結
    try:
        next_url = soup.find_all('a','next')[0]['href']
        #print(next_url)
    except Exception as e:
        print(e)
        next_url = None

    articles = []  # 儲存取得的文章資料
    divs = soup.find_all('a', 'js-article-link article-item floating-block-item')

    for d in divs:
        #print(d)
        if d.find('span', 'channel-signifier').string.strip() == region:  # 發文日期正確
            href = d.get('href')
            title = d.find('h4','article-title').string
            articles.append({
                'title': title,
                'href': href
            })
    return articles,next_url

#get image url
def parse(dom):
    try:
        soup = BeautifulSoup(dom, 'html.parser')

        links = soup.find('div','main-content').find_all('img')
        print(links)
        #print(links)
        img_urls = []
        for link in links:
            if re.match(r'^https?://', link['src']):
                img_urls.append(link['src'])

        # count = soup.findall('a','share-title').find('i',"icon icon-comment")
        # print('count:'+count)

        return img_urls
    except Exception:
        print(Exception)

def save(img_urls, title):
    if img_urls:
        try:
            dname = title.strip()  # 用 strip() 去除字串前後的空白
            if not os.path.exists(dname):
                os.makedirs(dname)
            for img_url in img_urls:
                if not img_url.endswith('.jpg'):
                    img_url += '.jpg'
                fname = time.strftime("%H%M%S")+".jpg"
                urllib.request.urlretrieve(img_url, os.path.join(dname, fname))
                time.sleep(1)
        except Exception as e:
            print(e)

if __name__ == "__main__":
    page = get_web_page('https://theinitium.com/channel/taiwan/')
    #page = get_web_page('https://theinitium.com/')
    if page:
        current_articles, next_url = get_articles(page,'台灣')
        articles = []

        while next_url is not None:  # 若目前頁面有今日文章則加入 articles，並回到上一頁繼續尋找是否有今日文章
            articles += current_articles
            current_page = get_web_page(WEB_URL +"/channel/taiwan/"+ next_url)
            current_articles, next_url = get_articles(current_page, '台灣')

        #articles = get_articles(page,'台灣')
        print(articles)
        print('____________')
        for post in articles:
            #print(post)
            page = get_web_page(WEB_URL + post['href'])
            img_urls = parse(page)
            print(img_urls)
            #save(img_urls, post['title'])
            post['num_image'] = len(img_urls)

        # save json
        with open('Newsdata.json', 'w', encoding='utf-8') as f:
            json.dump(articles, f, indent=2, sort_keys=True, ensure_ascii=False)