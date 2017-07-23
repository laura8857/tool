# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


def get_web_page(url):
    resp = requests.get(
        url=url,
    )

    if resp.status_code != 200:
        print('Invalid url:', resp.url)
        return None
    else:
        return resp.text


def get_articles(dom, date):
    soup = BeautifulSoup(dom, 'html.parser')

    articles = []  # 儲存取得的文章資料
    divs = soup.find_all('div', 'styles__horizontal-layout___2Sioo styles__header___3G557')
    print(divs)


    return articles


if __name__ == "__main__":
    page = get_web_page('https://test.deepblu.com/discover/live')
    # if page:
    #     #print(page)
    #     print('----------stop-----------')
