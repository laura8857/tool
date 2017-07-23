import os
from selenium import webdriver

class practice:

    def test(self):
        PATH = lambda p: os.path.abspath(
            os.path.join(os.path.dirname(__file__), p)
        )

        print("start Android")

        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        # desired_caps['browserName'] = ''
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps['deviceName'] = 'G3AZCY03J892'
        desired_caps['app'] = PATH(
            '/Users/huweiting/Desktop/laura/android-sdk-macosx/tools/app-internal2_2_9_3_170210_173325.apk')
        # desired_caps['app-package'] = 'com.example.android.contactmanager'
        # desired_caps['app-activity'] = '.ContactManager'

        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        driver.implicitly_wait(30)

        driver.find_element_by_id("textLogin").click()

        driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/editTextEmail").send_keys(
            "laura@deepblu.com")
        driver.back()
        driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/editTextPassword").send_keys("12345678")
        driver.back()
        driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/buttonSignUp").click()

if __name__=='__main__':
    practice=practice()
    practice.test()




