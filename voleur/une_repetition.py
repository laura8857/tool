# -*- coding: utf-8 -*-
#
# import requests
# from selenium import webdriver
#
# res = requests.get('http://pala.tw/js-example/')
# print(res.text)
# print("==========================================")
#
#
#
# driver = webdriver.PhantomJS(executable_path=r'/Users/huweiting/Desktop/phantomjs-2.1.1-macosx/bin/phantomjs')  # PhantomJs
# driver.get('https://dl.dropboxusercontent.com/u/11373114/NCU-HTML1031/HTML5Web1031/HelloForm.html')  # 輸入範例網址，交給瀏覽器
# pageSource = driver.page_source  # 取得網頁原始碼
# print(pageSource)
#
# driver.close()  # 關閉瀏覽器

import time
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome(executable_path=r'/Users/huweiting/Desktop/laura/chromedriver') # chrome瀏覽器
time.sleep(3)
driver.get('https://hahow.in/courses')

for i in range(10):  # 進行十次
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')  # 重複往下捲動
    time.sleep(1)  # 每次執行打瞌睡一秒

driver.close()  # 關閉瀏覽器