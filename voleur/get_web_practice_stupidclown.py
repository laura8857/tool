# -*- coding: utf-8 -*-
import json
import time
import requests
from bs4 import BeautifulSoup


PTT_URL = 'https://www.ptt.cc'


def get_web_page(url):
    time.sleep(0.5)  # 每次爬取前暫停 0.5 秒以免被 PTT 網站判定為大量惡意爬取
    resp = requests.get(
        url=url,
        cookies={'over18': '1'}
    )
    if resp.status_code != 200:
        print('Invalid url:', resp.url)
        return None
    else:
        return resp.text


def get_articles(dom):
    soup = BeautifulSoup(dom, 'html.parser')

    # 取得上一頁的連結
    paging_div = soup.find('div', 'btn-group btn-group-paging')
    prev_url = paging_div.find_all('a')[1]['href']

    articles = []  # 儲存取得的文章資料
    divs = soup.find_all('div', 'r-ent')
    for d in divs:
        # print("_______________________")
        # print(d.find('div', 'nrec').string)


        if d.find('span'):
            if d.find('a'):
                if d.find('div','nrec').string =='爆':
                    print(d.find('div', 'nrec').string)

                    # 取得文章連結及標題
                    if d.find('a'):  # 有超連結，表示文章存在，未被刪除
                        # print('href')
                        href = d.find('a')['href']
                        title = d.find('a').string
                        articles.append({
                            'title': title,
                            'href': href,
                            'push_count': 2000
                        })

                if d.find('div','nrec').string !='爆':
                    pushcount = int(d.find('div', 'nrec').string)
                    if pushcount>50:
                        print(d.find('div', 'nrec').string)

                        href = d.find('a')['href']
                        title = d.find('a').string
                        articles.append({
                            'title': title,
                            'href': href,
                            'push_count': pushcount
                        })
    return articles,prev_url


def get_content(dom):
    soup = BeautifulSoup(dom, 'html.parser')

    divs = soup.find('div', 'bbs-screen bbs-content')
    # print(divs)
    content = str(divs)
    try:
        #
        # sourse_code = requests.get('https://www.ptt.cc/bbs/StupidClown/M.1498480963.A.F74.html').text
        # soup = BeautifulSoup(sourse_code, "html.parser")
        # content = soup.select('#main-content')
        # [d.extract() for d in content[0].select('div')]
        # [d.extract() for d in content[0].select('span')]
        # content_info = content[0].getText()
        # print(content_info)
        #delete author title time
        title = divs.find_all('div','article-metaline')
        for d in title:
            # print(d)
            content = content.replace(str(d),'')

        # delete metatag
        metatag = divs.find('div','article-metaline-right')
        # print(metatag)
        content =content.replace(str(metatag),'')

        # delete info
        info = divs.find_all('span','f2')
        for i in info:
            # print(i)
            content = content.replace(str(i), '')

        # delete push
        push = divs.find_all('div','push')
        for p in push:
            # print(p)
            content = content.replace(str(p),'')

        # delete img
        img = divs.find_all('div','richcontent')
        for im in img:
            content = content.replace(str(im),'')

        # delete other
        content = content.replace('<div class="bbs-screen bbs-content" id="main-content">','')
        content = content.replace('</div>', '')

        span = divs.find_all('span')
        for s in span:
            content = content.replace(str(s),'')


        # delete link
        link = divs.find_all('a')
        for a in link:
            # print(a)
            content = content.replace(str(a),'')

        # print(content)
        return content
    except Exception as e:
        print(e)



if __name__ == "__main__":
    current_page = get_web_page(PTT_URL + '/bbs/StupidClown/index3410.html')
    # page = get_web_page('https://www.ptt.cc/bbs/StupidClown/index3410.html')
    if current_page:

        articles = []  # 全部的今日文章
        date = time.strftime("%m/%d").lstrip('0')  # 今天日期, 去掉開頭的 '0' 以符合 PTT 網站格式
        current_articles, prev_url = get_articles(current_page)  # 目前頁面的今日文章

        while current_articles:  # 若目前頁面有今日文章則加入 articles，並回到上一頁繼續尋找是否有今日文章
            articles += current_articles
            current_page = get_web_page(PTT_URL + prev_url)
            current_articles, prev_url = get_articles(current_page)

        for post in articles:
            print(post)


        for article in articles:
            page = get_web_page(PTT_URL + article['href'])
            if page:
                # print(page)
                content = get_content(page)
                article['content'] = content


        # save json
        with open('stupidData.json', 'w', encoding='utf-8') as f:
            json.dump(articles, f, indent=2, sort_keys=True, ensure_ascii=False)



# sourse_code = requests.get('https://www.ptt.cc/bbs/StupidClown/M.1498480963.A.F74.html').text
# soup = BeautifulSoup(sourse_code, "html.parser")
# content = soup.select('#main-content')
# [d.extract() for d in content[0].select('div')]
# content_info = content[0].getText()



