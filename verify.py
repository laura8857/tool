# -*- coding: utf-8 -*-


import requests
from admin_token import admin_token

#驗證 link
def verify_by_link(url):
    json = {"accept-language": "en"}
    res = requests.get(url,headers=json)


def getusercode(email):
    token = admin_token()
    url = "http://test.tritondive.co:3000/1/api/users?access_token="+token+ \
          "&filter={\"where\":{\"email\":\"" + email + "\"}}"
    result = requests.get(url)
    if result.status_code == 200:
        if len(result.json()) == 1:
            user_code = ""
            user_code = result.json()[0]['code']
            print("usercode:" + str(user_code))
            link = "https://test.tritondive.co/apis/user/v0/activeAccount?ownerId=" + result.json()[0][
                'id'] + "&code=" + user_code
            dict = {"code": user_code, "link": link}
            return dict
        else:
            return {}


def verify(email):
    verifydict = {}
    verifydict = getusercode(email)
    if len(verifydict) == 0:
        print("Verify failed/")
    else:
        link = verifydict["link"]
        verify_by_link(link)
        print('Send notification.Verify successfully!')

if __name__ == "__main__":
    verify('aladin@deepblu.com')