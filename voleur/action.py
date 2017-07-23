# -- coding: utf-8 --

from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def set_up():
    global driver
    try:
        driver = webdriver.Chrome(executable_path=r'/Users/huweiting/Desktop/auto_'
                                                   r'test/automation/Social_Web/chromedriver_2_29')
    except Exception as e:
        print(e)

def login():
    try:
        sleep(3)
        driver.get("https://zh-tw.facebook.com/")
        sleep(3)
        # wait('id','email')
        driver.find_element_by_id('email').send_keys('andxxxd@gmail.com')
        sleep(3)
        driver.find_element_by_id('pass').send_keys('androidxxx')
        # click login button
        driver.find_element_by_id('u_0_r').click()
        sleep(5)
        driver.find_element_by_xpath('//*[@id="facebook"]/body/div[21]/div[2]/div/div/div/div/div[3]/div/div/div[2]/div/a[2]').click()

    except Exception as e:
        print(e)

def messager(like=None,id=None):
    try:
        if like ==None:
            like=5
        if id == None:
            id = '100014218267258'
        # driver.get('https://www.facebook.com/profile.php?id=100014170658669')
        driver.get('https://www.facebook.com/profile.php?id='+id)
        sleep(5)
        # driver.find_element_by_xpath('//*[@id="facebook"]/body/div[27]/div[2]/div/div/div/div/div[3]/div/div/div[2]/div/a[1]').click()
        driver.find_element_by_css_selector('body > div._10.uiLayer._4-hy._3qw > div._59s7 > div > div > div > div > div._5a8u._5lnf.uiOverlayFooter > div > div > div._ohf.rfloat > div > a.layerCancel._4jy0._4jy3._517h._51sy._42ft').click()


        sleep(5)
        #click send message window  不同帳號的send message button id 不一樣欸 ＝＝
        try:
            driver.find_element_by_id('u_0_x').click()
            driver.find_element_by_id('u_0_v').click()

        except Exception as e:

            print(Exception)

        sleep(5)

        # click like button
        i = 0
        while i < like:
            driver.find_element_by_css_selector('a._5j_u._6gb > svg > g > g > path').click()
            i+=1
            sleep(2)

        # likebutton = driver.find_element_by_css_selector('a._5j_u._6gb > svg > g > g > path')
        # actions = ActionChains(driver)
        # sleep(2)
        #
        # actions.click_and_hold(likebutton).perform()
    except Exception as e:
        print(e)




    except Exception as e:
        print(e)
def sleep(second):
    time.sleep(second)

def wait(type=None,el=None,second=None):
    try:
        if type == 'id':
            type = By.ID
        elif type == 'class':
            type = By.CLASS_NAME
        elif type == 'name':
            type = By.NAME
        elif type == 'tag':
            type = By.TAG_NAME
        elif type == 'xpath':
            type = By.XPATH
        else:
            type = By.ID

        if second == None:
            second = 20

        WebDriverWait(driver, second).until(EC.visibility_of_element_located(type,el))
    except Exception as e:
        print("[Error] The element: %s can't be found. %s" % (el, e))
