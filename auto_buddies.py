# -*- coding: utf-8 -*-
# @Time    : 2017/4/24 上午10:36
# @Author  : Yuhsuan
# @File    : auto_buddies.py
# @Software: PyCharm Community Edition
# 自動建立帳號
# 自動增加好友

# 1. 請先安裝requests, pip install requests

import requests
import datetime

class auto_buddies():
    def __init__(self):
        now = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S')

        self.Server = 'test'
        self.pwd='123456'
        self.headers = {"accept-language":"en"}

        self.server_setting(self.Server)

    def server_setting(self,type):
        if type == 'test':
            self.apiServer = "http://test.tritondive.co:8000/"
            self.apiServer2 = "http://test.tritondive.co:3000/"
            self.apiServer3 = "https://test.tritondive.co/"
        else:
            self.apiServer = "http://dev.tritondive.co:8000/"
            self.apiServer2 = "http://dev.tritondive.co:3000/"
            self.apiServer3 = "https://dev.tritondive.co/"

    def checkEmail(self,email):
        check_body = {"email": email}
        res = requests.post(self.apiServer + "apis/user/v0/checkEmail", headers=self.headers, data=check_body)
        if res.status_code == 200:
            print(res.text)
            if "duplicate" in res.json()["result"]:
                if res.json()['result']['duplicate'] == "n":
                    return False
                else:
                    return True
            else:
                return False
        else:
            return False

    def get_verify_code(self,email):
        url = self.apiServer2+"1/api/users?access_token=YnlyhlAnurDmKOsknbEcR1tuyvrX6Xr9wRR5fwq79WwrQtOlgRC9sQmKmzYAfqqy&filter={\"where\":{\"email\":\"" + email + "\"}}"
        result = requests.get(url)
        #print(result.text)
        if result.status_code == 200:
            if len(result.json()) == 1:
                code = result.json()[0]['code']
                link = self.apiServer3+"apis/user/v0/activeAccount?ownerId=" + result.json()[0]['id'] + "&code=" + code
                dict = {"code": code, "link": link}
                #print(dict)
                return dict
            else:
                return {}

    # 檢查是否已存在帳號，如果不是就建立
    def register(self,email,pwd=None):
        if not self.checkEmail(email.lower()):
            if pwd==None:
                pwd = self.pwd
            userName = email[:email.find("@")]
            register_body={"email":email.lower(),"password":pwd,"userName":userName,"deviceId": ""}
            res = requests.post(self.apiServer+"apis/user/v0/register",headers=self.headers,data=register_body)
            if res.status_code==200:
                #time.sleep(5)
                #print(get_verify_code(email.lower()))
                url = self.get_verify_code(email.lower())
                url = url['link']
                res = requests.get(url, headers={"accept-language": "en"})
                print("註冊成功")
            else:
                #print(res.status_code)
                print("註冊失敗")
        else:
            print("重複email")

    def login(self,email,pwd=None):
        if pwd == None:
            pwd = "123456"
        login_data={"email": email,"password": pwd,"deviceId": "string"}
        res = requests.post(self.apiServer+"apis/user/v0/login",headers=self.headers,data=login_data)
        if res.status_code==200:
            result = [email,res.json()["result"]["accessToken"],res.json()["result"]["userInfo"]["ownerId"]]
        else:
            result=[email,"",""]
        return result

    def buddy_request(self,list):
        self.headers["authorization"] = list[0][1]
        buddy_data = {"buddyUserId":list[1][2]}
        res = requests.post(self.apiServer+"apis/buddy/v0/request",headers=self.headers,data=buddy_data)
        print(res.text)

    def buddy_approve(self,list):
        self.headers["authorization"] = list[1][1]
        buddy_data = {"buddyUserId": list[0][2]}
        res = requests.put(self.apiServer + "apis/buddy/v0/approve", headers=self.headers, data=buddy_data)
        print(res.text)

    def buddies(self,group):
        for i in range(0,len(group)-1):
            for j in  range(i+1,len(group)):
                self.buddy_request([group[i],group[j]])
                self.buddy_approve([group[i], group[j]])

    def change_password(self,email,oldpwd,newpwd):
        info = self.login(email,oldpwd)
        self.headers["authorization"]=info[1]
        pwd={"oldPassword": oldpwd,"newPassword": newpwd}
        res = requests.post(self.apiServer+"apis/user/v0/changePassword",headers=self.headers,data=pwd)

        print(res.text)

if __name__=="__main__":

    buddies = auto_buddies()

    # 設定Server, 'test' or 'dev'
    buddies.Server = 'dev'
    buddies.server_setting(buddies.Server)

    # 設定預設密碼
    buddies.pwd = '123456'

    # 你要新增加帳號以及建立好友清單的帳號們
    buddy = ["yuhsuan@deepblu.com"]
    # buddy.append('test01@test.com')
    # buddy.append('test02@test.com')
    # buddy.append('test03@test.com')
    # buddy.append('test04@test.com')

    # 這邊會開始執行邏輯
    group=[]
    for i in buddy:
        buddies.register(i)
        group.append(buddies.login(i))

    print(group)
    buddies.buddies(group)