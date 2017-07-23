# -*- coding: utf-8 -*-
# @Time    : 2017/3/24 下午5:40
# @Author  : Yuhsuan
# @File    : token_expired.py
# @Software: PyCharm Community Edition

from pymongo import *
import requests

def token_expired(email):
    # connect to mongo
    client = MongoClient("52.197.14.177", 27017)
    client.deepblu.authenticate('deepblu2', 'DGeANYhWyx8prMFgYEj6', mechanism='MONGODB-CR')
    db = client.deepblu

    if db.user.find_one({"email":email}):
        user = {}
        token =""
        user = db.user.find_one({"email": email})
        id = user['_id']
        print(str(id))

        for doc in db.AccessToken.find({"userId":id}).sort("created",-1).limit(1):
            token = doc['_id']
            print(token)

        #call api
        url = "http://test.tritondive.co:8000/apis/user/v0/tokenExpire"
        data = {}
        data['accessToken']=token
        headers = {"Accept-Language": "en"}
        result = requests.post(url,json=data,headers = headers)
        if result.status_code == 200:
            print(result.text)
    else:
        print("The mail "+email+" can't be found.")
    client.close()

if __name__ == "__main__":
    token_expired('hi@deepblu.com')