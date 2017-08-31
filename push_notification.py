# -*- coding: utf-8 -*-
# @Time    : 2017/2/13 下午2:50
# @Author  : Yuhsuan
# @File    : deepblu_api.py
# @Software: PyCharm Community Edition

# link : http://test.tritondive.co:3000/explorer/
# Token : YnlyhlAnurDmKOsknbEcR1tuyvrX6Xr9wRR5fwq79WwrQtOlgRC9sQmKmzYAfqqy

import requests
from datetime import datetime
from urllib.parse   import quote
from admin_token import admin_token

# GET /users
def get_users(email):
    global token
    token = admin_token()
    url = 'http://test.tritondive.co:3000/1/api/users?filter=%7B%22where%22%3A%7B%22email%22%3A%22'+ email+'%22%7D%7D&access_token='+token
    result = requests.get(url)
    return result.json()

# POST /NotificationLogs/genNotifData
# content: 顯示的內容
# url: deepblu link or else
# type: single|multi|APNS|GCM|All
# userid: e.g. 587db9693119400d12826869
def send_push_msg(content, url, time, type, user_id):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = now + ' ' + content

    #url = 'http://test.tritondive.co:3000/1/api/NotificationLogs/genNotifData?access_token=HGrcok0m2O2n6XID8CJXz8HrtE5ZF8w2Yq6MmTTF4Aqnpix18mDBhGhsCAkWRMRY&ownerId=5810900c078dd4630b276265&msg=test123dddd&url=deepblu%3A%2F%2Fdeepblu.link%2FCommunity%2FYourGroups%2Fgroup%3FgroupId%3D541&mode=single&expTime=2017-02-18T12%3A09%3A22%2B08%3A00'
    url = 'http://test.tritondive.co:3000/1/api/NotificationLogs/genNotifData?access_token='+token+'&ownerId='+user_id+'&msg='+content+'&url='+url+'&mode='+type+'&expTime='+quote(time)

    result = requests.post(url)
    print("url:"+url)
    if result.status_code==200:
        print('Send push message success')
    else:
        print('Please check with a ming for api')


if __name__ == "__main__":
    # Get
    dict = {}
    result = get_users('laura4@deepblu.com')
    dict = result[0]
    user_id = dict['id']

    print("userid: "+user_id)

    # Post message to user
    content = 'test message'
    url = 'https://www.google.com.tw/'
    time="2017-02-18T12:09:22+08:00"


    type = 'single'
    # single|multi|APNS|GCM|All
    #user_id = '587db9693119400d12826869'
    send_push_msg(content,url,time,type,user_id)
