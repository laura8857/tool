# -*- coding: utf-8 -*-

from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'/Users/huweiting/Desktop/laura/chromedriver')
driver.get('http://www.pixiv.net/')
driver.save_screenshot('儲存位置/檔案名稱.png')  # 保存截圖
driver.close()