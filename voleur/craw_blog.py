# -*- coding: utf-8 -*-
import requests
import os
from bs4 import BeautifulSoup
import re
import pandas as pd
import time
import datetime
import pymysql
from datetime import datetime as dtime


def get_ptt_data(article_url):
    res2 = requests.get(article_url, verify=True)  # 擷取該網站 原始碼
    soup2 = BeautifulSoup(res2.text, "lxml")  # beautiful 漂亮的呈現原始碼


    # print(soup2)


def main_craw_blog():
    ptt_class_name = 'Soft_Job'
    index_name = 'http://www.ptt.cc'
    index_class = '/bbs/' + ptt_class_name + '/index'
    i=1299

    index_url = index_name + index_class + str(i) + '.html'  # 抓第 i 個目錄
    # res = requests.get(index_url,verify = False)
    index_url="https://howtorapeurjob.tumblr.com/"
    res = requests.get(index_url, verify=True)  # 讀取 html 原始碼
    soup = BeautifulSoup(res.text, "lxml")  # html轉為漂亮   幫助觀察原始碼

    # print(soup)

    divs = soup.find_all("", {'class': 'post-panel'})

    article =[]

    for d in divs:
        print(str(d.find("",{'class':'post-title'}).text))
        # linkcontent = d.find('p','read_more_container')


        # print(title)


    print(divs)

if __name__ == "__main__":
    # link="https://www.ptt.cc/bbs/Soft_Job/M.1503652456.A.526.html"
    # get_ptt_data(link)

    main_craw_blog()
