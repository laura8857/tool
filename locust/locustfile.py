# -*- coding: utf-8 -*-
# @Time    : 2017/4/7 下午2:52
# @Author  : Yuhsuan
# @File    : locustfile.py.py
# @Software: PyCharm Community Edition
from locust import *

# 每次都進入index
def index(l):
    pass

# apis/trending

# GET /apis/trending/v0/slider, Social_Web 取得 Trending Sliders
def TrendingSlider(l):
    header = {"accept-language":"en"}
    res = l.client.get("/apis/trending/v0/slider",headers=header)

# GET /apis/trending/v0/slider/mobile, mobile 取得 Trending Sliders
def TrendingSliderMobile(l):
    header = {"accept-language":"en"}
    res = l.client.get("/apis/trending/v0/slider/mobile",headers=header)

# apis/user

# GET /apis/user/v0/suggestDiver
def UserSuggestDiver(l):
    header = {"accept-language":"en"}
    res = l.client.get("/apis/user/v0/suggestDiver",headers=header)

# apis/follow

# apis/group
# GET /apis/group/v0/all
def GroupALl(l):
    header = {"accept-language":"en"}
    res = l.client.get("/apis/group/v0/all?skip=0&limit=10&orderCriteria=popularity",headers=header)

# GET /apis/group/v0/search
def GroupSearch(l):
    header = {"accept-language":"en"}
    res = l.client.get("/apis/group/v0/search?skip=0&limit=10&orderCriteria=popularity",headers=header)

# apis/reseller
# GET /apis/reseller/v0/language
def ResellerLanguage(l):
    header = {"accept-language":"en"}
    res = l.client.get("/apis/reseller/v0/language",headers=header)

# GET /apis/reseller/v0/payment-method
def ResellerPaymentMethod(l):
    header = {"accept-language":"en"}
    res = l.client.get("/apis/reseller/v0/payment-method",headers=header)

# apis/buddy

# apis/discover
# GET /apis/discover/v0/post/diveLogFeed
def DiscoverPostDiveLogFeed(l):
    header = {"accept-language": "en"}
    res = l.client.get("/apis/discover/v0/post/diveLogFeed?limit=10&skip=0", headers=header)

# GET /apis/discover/v0/post/liveFeed
def DiscoverPostLiveFeed(l):
    header = {"accept-language":"en"}
    res = l.client.get("/apis/discover/v0/post/liveFeed?skip=10&limit=10",headers=header)

# GET /apis/discover/v0/post/search
def DiscoverPostSearch(l):
    header = {"accept-language":"en"}
    res = l.client.get("/apis/discover/v0/post/search?limit=10&skip=0",headers=header)

# GET /apis/discover/v0/post/trendingFeed
def DiscoverPostTrendingFeed(l):
    header = {"accept-language":"en"}
    res = l.client.get("/apis/discover/v0/post/trendingFeed?limit=10&skip=0",headers=header)

# apis/entity

# apis/divelog

# apis/media

# apis/notification

# apis/slidePanel
# GET /apis/slidePanel/v0/allSlide
def SlidePanel(l):
    header = {"accept-language":"en"}
    res = l.client.get("/apis/slidePanel/v0/allSlide",headers=header)

class UserBehavior(TaskSet):
    tasks = {
        TrendingSlider:10,
        TrendingSliderMobile:10,
        UserSuggestDiver:10,
        GroupALl:10,
        GroupSearch:10,
        ResellerLanguage:10,
        ResellerPaymentMethod:10,
        DiscoverPostDiveLogFeed:10,
        DiscoverPostLiveFeed:10,
        DiscoverPostSearch:10,
        DiscoverPostTrendingFeed:10,
        SlidePanel:10
    }

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    # 每個task之間的間隔時間,預設最大最小時間為一秒,單位為毫秒
    min_wait = 60000
    max_wait = 3600000