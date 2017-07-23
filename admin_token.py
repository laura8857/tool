# -*- coding: utf-8 -*-
# @Time : Thu May 11 18:09:48 2017 +0800
# @Author : Laura(laura@deepblu.com)

#Get New Token

import requests

def login(email,password):

    # call login api to get id
    url='http://test.tritondive.co:3000/1/api/users/login'
    data={}
    data['email']=email
    data['password']=password
    result = requests.post(url, json=data)
    if result.status_code == 200:
        print('Login Success.')
        dict = {}
        dict=result.json()
        id = dict['id']
        # print(result.text)
        print('id:'+id)
        return id
    else:
        print("Login failed.")


def admin_token():
    email = 'laura@deepblu.com'
    password='12345678'
    id = login(email,password)

    # call admim's api
    url = 'http://test.tritondive.co:3000/1/api/users/asAdmin'
    data = {}
    data['password'] = id
    result = requests.post(url, json=data)
    if result.status_code == 200:
        print('admin Success.')
        # print(result.text)
        dict = {}
        dict = result.json()
        resultdict = {}
        resultdict = dict['response']
        token = resultdict['id']
        print('token:'+token)
        return token
    else:
        print('admin failed.')

if __name__ == "__main__":
    admin_token()
