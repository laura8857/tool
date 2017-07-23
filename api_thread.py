# -*- coding: utf-8 -*-
# @Time    : 2017/4/7 下午6:26
# @Author  : Yuhsuan
# @File    : api.py
# @Software: PyCharm Community Edition

import threading
import time
import requests
import queue

def time_usage(func):
    def wrapper(*args, **kwargs):
        global timeExec
        global q

        beg_ts = time.time()
        try:
            res = func(*args, **kwargs)
            end_ts = time.time()
            timeExec = end_ts - beg_ts
        except:
            res = False
            timeExec=0
        # print(u"耗時: %.10f" % (timeExec))
        dic = {"name":func.__name__,"result":res,"time":timeExec}
        # print(dic)
        q.put(dic)
    return wrapper

def Run(num,func):
    global q
    q = queue.Queue(num)

    # Thread pool
    th = []

    for i in range(num):
        t = threading.Thread(target=func,name="t.%d" % i)
        th.append(t)
    # start thread
    for i in th:
        i.start()

    # wait for all thread
    for i in th:
        i.join()
    return summary(num)

def summary(num):
    global q
    # result pool
    res_pool = []
    # time pool
    time_pool = []
    # name
    name =""
    for i in range(num):
        res = q.get()
        time_pool.append(res['time'])
        res_pool.append(res['result'])
        name = res['name']

    fail_count = 0
    for i in res_pool:
        if i==False:
            fail_count = fail_count+1

    result = {}
    result['test_case']=name
    result['avg_time']=(sum(time_pool) / len(time_pool))
    result['max_time']=max(time_pool)
    result['min_time']=min(time_pool)
    result['fail_rate']="fail: %s, total: %s" % (fail_count,num)

    print(result)
    print("Delay 3 sec for next test")
    time.sleep(3)
    return result

'''
@time_usage
# http://test.tritondive.co:8000/apis/trending/v0/slider
def TrendingSlider():
    header = {"accept-language":"en"}
    res = requests.get("http://test.tritondive.co:8000/apis/trending/v0/slider",headers=header,timeout=10)
    if res.status_code!=200:
        return False
    else:
        return True

@time_usage
# GET /apis/trending/v0/slider/mobile, mobile 取得 Trending Sliders
def TrendingSliderMobile():
    header = {"accept-language":"en"}
    res = requests.get("http://test.tritondive.co:8000/apis/trending/v0/slider/mobile",headers=header,timeout=10)
    if res.status_code!=200:
        return False
    else:
        return True

@time_usage
# GET /apis/trending/v0/slider/mobile, mobile 取得 Trending Sliders
def test():
    header = {"accept-language":"en"}
    res = requests.get("https://github.com/locustio/locust",timeout=10)
    if res.status_code!=200:
        return False
    else:
        return True
'''

# apis/trending

# GET /apis/trending/v0/slider, Social_Web 取得 Trending Sliders
@time_usage
def TrendingSlider():
    header = {"accept-language":"en"}
    res = requests.get("http://test.tritondive.co:8000/apis/trending/v0/slider",headers=header,timeout=10)
    if res.status_code!=200:
        return False
    else:
        return True

# GET /apis/trending/v0/slider/mobile, mobile 取得 Trending Sliders
@time_usage
def TrendingSliderMobile():
    header = {"accept-language":"en"}
    res = requests.get("http://test.tritondive.co:8000/apis/trending/v0/slider/mobile",headers=header,timeout=10)
    if res.status_code!=200:
        return False
    else:
        return True

# apis/user

# GET /apis/user/v0/suggestDiver
@time_usage
def UserSuggestDiver():
    header = {"accept-language":"en"}
    res = requests.get("http://test.tritondive.co:8000/apis/user/v0/suggestDiver",headers=header,timeout=10)
    if res.status_code!=200:
        return False
    else:
        return True

# apis/follow

# apis/group
# GET /apis/group/v0/all
@time_usage
def GroupALl():
    header = {"accept-language":"en"}
    res = requests.get("http://test.tritondive.co:8000/apis/group/v0/all?skip=0&limit=10&orderCriteria=popularity",headers=header,timeout=10)
    if res.status_code!=200:
        return False
    else:
        return True

# GET /apis/group/v0/search
@time_usage
def GroupSearch():
    header = {"accept-language":"en"}
    res = requests.get("http://test.tritondive.co:8000/apis/group/v0/search?skip=0&limit=10&orderCriteria=popularity",headers=header,timeout=10)
    if res.status_code!=200:
        return False
    else:
        return True

# apis/reseller
# GET /apis/reseller/v0/language
@time_usage
def ResellerLanguage():
    header = {"accept-language":"en"}
    res = requests.get("http://test.tritondive.co:8000/apis/reseller/v0/language",headers=header,timeout=10)
    if res.status_code!=200:
        return False
    else:
        return True

# GET /apis/reseller/v0/payment-method
@time_usage
def ResellerPaymentMethod():
    header = {"accept-language":"en"}
    res = requests.get("http://test.tritondive.co:8000/apis/reseller/v0/payment-method",headers=header,timeout=10)
    if res.status_code!=200:
        return False
    else:
        return True

# apis/buddy

# apis/discover
# GET /apis/discover/v0/post/diveLogFeed
@time_usage
def DiscoverPostDiveLogFeed():
    header = {"accept-language": "en"}
    res = requests.get("http://test.tritondive.co:8000/apis/discover/v0/post/diveLogFeed?limit=10&skip=0", headers=header,timeout=10)
    if res.status_code!=200:
        return False
    else:
        return True

# GET /apis/discover/v0/post/liveFeed
@time_usage
def DiscoverPostLiveFeed():
    header = {"accept-language":"en"}
    res = requests.get("http://test.tritondive.co:8000/apis/discover/v0/post/liveFeed?skip=10&limit=10",headers=header,timeout=10)
    if res.status_code!=200:
        return False
    else:
        return True

# GET /apis/discover/v0/post/search
@time_usage
def DiscoverPostSearch():
    header = {"accept-language":"en"}
    res = requests.get("http://test.tritondive.co:8000/apis/discover/v0/post/search?limit=10&skip=0",headers=header,timeout=10)
    if res.status_code!=200:
        return False
    else:
        return True

# GET /apis/discover/v0/post/trendingFeed
@time_usage
def DiscoverPostTrendingFeed():
    header = {"accept-language":"en"}
    res = requests.get("http://test.tritondive.co:8000/apis/discover/v0/post/trendingFeed?limit=10&skip=0",headers=header,timeout=10)
    if res.status_code!=200:
        return False
    else:
        return True

# apis/entity

# apis/divelog

# apis/media

# apis/notification

# apis/slidePanel
# GET /apis/slidePanel/v0/allSlide
@time_usage
def SlidePanel():
    header = {"accept-language":"en"}
    res = requests.get("http://test.tritondive.co:8000/apis/slidePanel/v0/allSlide",headers=header,timeout=10)
    if res.status_code!=200:
        return False
    else:
        return True

if __name__=="__main__":
    try:
        Run(10,TrendingSlider)
        Run(10,TrendingSliderMobile)
        Run(10,UserSuggestDiver)
        Run(10,GroupALl)
        Run(10,GroupSearch)
        Run(10,ResellerLanguage)
        Run(10,ResellerPaymentMethod)
        Run(10,DiscoverPostDiveLogFeed)
        Run(10,DiscoverPostLiveFeed)
        Run(10,DiscoverPostSearch)
        Run(10,DiscoverPostTrendingFeed)
        Run(10,SlidePanel)
        #Run(10,test)
    except Exception as e:
        print(e)