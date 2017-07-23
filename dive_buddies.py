# -*- coding: utf-8 -*-

import requests
from admin_token import admin_token

def get_api(link):
    res = requests.get(link)
    text = res.json()
    return text

def dive_buddies(postId):
    #找logId
    global token
    token= admin_token()
    api_link = "http://test.tritondive.co:3000/1/api/Posts/" + postId + "?access_token="+token
    dict = {}
    dict = get_api(api_link)

    logId = dict['diveLogId']
    print("logId:" + logId)

    # 找dive buddies 跟 dive buddies waitlist
    api_link_log = "http://test.tritondive.co:3000/1/api/LogDives/"+logId+"?access_token="+token
    dict2 = {}
    dict2 = get_api(api_link_log)
    diveBuddies = {}
    instructor = ""
    try:
        diveBuddies = dict2['diveBuddies']

        print("dive buddies list :" )
        for item in diveBuddies:
            if getUserName(item) ==None:
                print(getEmail(item))
            else:
                print(getUserName(item)+"("+getEmail(item)+")")
    except Exception:
        print("There is no dive buddies.")

    try:
        waitBuddies = dict2['diveBuddiesWaitList']
        print("\ndive buddies wait list:")
        for item2 in waitBuddies:
            if getUserName(item2)==None:
                print(getEmail(item2))
            else:
                print(getUserName(item2)+"("+getEmail(item2)+")")
    except Exception:
        print("There is no waiting dive buddies.")

    try:
        instructor = dict2['approveBy']
        print("\ninstructor:"+getUserName(instructor)+"("+getEmail(instructor)+")")
        approveStatus = dict2['approveStatus']
        print('approveStatus:'+approveStatus)

    except Exception:
        print("\nThere is no instructor")




def getEmail(ownerId):
    api_link_email="http://test.tritondive.co:3000/1/api/users/"+ownerId+"?access_token="+token
    dictEmail = {}
    dictEmail = get_api(api_link_email)

    email = dictEmail['email']
    return email

def getUserName(ownerId):
    try:
        api_link_name = "http://test.tritondive.co:3000/1/api/dusers?filter=%7B%22where%22%3A%7B%22ownerId%22%3A%22"+ownerId+"%22%7D%7D&access_token="+token
        dictName={}
        dictName = get_api(api_link_name)

        userInfo = {}
        userInfo = dictName[0]
        userName = userInfo['userName']

        return userName

    except Exception:
        return None


if __name__ == "__main__":
    #輸入dive log的postId
    dive_buddies("b16ffad06b6e11e7aa140d17024777c7")
