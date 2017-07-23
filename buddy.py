# -*- coding: utf-8 -*-

from pymongo import *
import requests

buddylist = ['laura@deepblu.com', 'laura2@deepblu.com', 'laura3@deepblu.com', 'laura4@deeepblu.com', 'mei@deepblu.com']


def buddy(email):
    # connect to mongo
    client = MongoClient("52.197.14.177", 27017)
    client.deepblu.authenticate('deepblu2', 'DGeANYhWyx8prMFgYEj6', mechanism='MONGODB-CR')
    db = client.deepblu

    if db.user.find_one({"email": email}):
        user = {}
        token = ""
        user = db.user.find_one({"email": email})
        id = user['_id']
        # print(str(id))

        for doc in db.AccessToken.find({"userId": id}).sort("created", -1).limit(1):
            token = doc['_id']
            print(token)

        # post
        url = "http://test.tritondive.co:8000/apis/buddy/v0/request"
        data = {}
        buddy_user = db.user.find_one({"email": 'laura@deepblu.com'})
        buddy_id = buddy_user['_id']
        data['buddyUserId'] = str(buddy_id)
        headers = {"Accept-Language": "en","authorization": token}
        result = requests.post(url, json=data, headers=headers)
        if result.status_code == 200:
            print(result.text)

            url2 = "http://test.tritondive.co:8000/apis/buddy/v0/approve"

        else:
            print(result.text)


    else:
        print("The mail " + email + " can't be found.")
    client.close()

def getuserId(email):
    client = MongoClient("52.197.14.177", 27017)
    client.deepblu.authenticate('deepblu2', 'DGeANYhWyx8prMFgYEj6', mechanism='MONGODB-CR')
    db = client.deepblu

    if db.user.find_one({"email": email}):
        user = {}
        token = ""
        user = db.user.find_one({"email": email})
        id = user['_id']

    else:
        print("The mail " + email + " can't be found.")
    client.close()


#def gettoken(userId):



if __name__ == "__main__":
    buddy('mei@deepblu.com')
