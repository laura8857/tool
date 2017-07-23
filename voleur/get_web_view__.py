# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


def get_web_page(url):
    resp = requests.get(
        url=url,
        cookies={'over18': '1'}
    )
    if resp.status_code != 200:
        print('Invalid url:', resp.url)
        return None
    else:
        return resp.text


def get_article():

    sourse_code = requests.get('https://www.ptt.cc/bbs/StupidClown/M.1498480963.A.F74.html').text
    soup = BeautifulSoup(sourse_code, "html.parser")
    content = soup.select('#main-content')
    [d.extract() for d in content[0].select('div')]
    [d.extract() for d in content[0].select('span')]
    content_info = content[0].getText()
    print(content_info)


if __name__ == "__main__":
    get_article()

    # page = get_web_page('https://www.ptt.cc/bbs/Beauty/index.html')
    # if page:
    #     print(page)