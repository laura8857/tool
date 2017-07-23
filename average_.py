# -*- coding: utf-8 -*-
import null as null
import requests
import time
from admin_token import admin_token

def get_api(link):
    timeExec = 0.0
    beg_ts = time.time()
    res = requests.get(link)
    end_ts = time.time()

    timeExec = end_ts - beg_ts
    text = res.json()
    print(u"Cost Time: %.5f secs" % timeExec)
    return text


if __name__ == "__main__":
    token = admin_token()
    divelogID="58f5b246f709e7e54de4e33f"
    api_link='http://test.tritondive.co:3000/1/api/LogDives/'+divelogID+'?access_token='+token
    result = get_api(api_link)
    #print(result)
    dict = {}
    temp = {}
    dict = result
    divelog = []


    divetime=dict['diveDT']
    print("divetime:"+divetime)

    # 0:淡水->100 預設是淡水
    # 1:鹹水-->102.5

    if('waterType' in dict):
     if dict['waterType']==1:
        watertype=102.5
     else:
        watertype=100

    else:
        watertype=100

    print("watertype:" + str(watertype))


    #airPressure 沒有值得話 設定1000
    if('airPressure' in dict):
        airPressure=dict['airPressure']
    else:
        airPressure=1000

    print("airPressure:" + str(airPressure))
    diveProfile={}
    diveProfile=dict['_diveProfile']
    allprofile=len(diveProfile)
    print("allprofile:"+str(allprofile))

    for items in range(0,allprofile):
        temp=diveProfile[items]
        divelog.append(temp['pressure'])


    print(divelog)
    print("Total is "+ str(sum(divelog)))

    # [(logDive._diveProfile.pressure 加總 ÷ profile總數) - air pressure] / waterType
    average=((sum(divelog)/allprofile)-airPressure)/watertype
    #average=round(sum(divelog)/allprofile,1)
    print("sum(divelog)/allprofile:"+str(sum(divelog)/allprofile))
    #average=(average-airPressure)/watertype
    print("average1:"+str(round(average,1))+" m")
    print("average2:" + str(average)+" m")