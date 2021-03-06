# -*- coding: utf-8 -*-
'''
@Date: 2017/02/10
@Description: For average depth spec
'''
import sys
import deepblu_api

# 最大深度與Cosmiq同步，小數點一位無條件捨去

# m to ft
ft = 3.2808399
def get_raw_divelog(email):
    token = deepblu_api.get_token(email)
    divelogs = deepblu_api.get_divelogs(token)
    # l = len(divelogs)
    # for i in range(0,l):
    #     average_depth(divelogs[l-i-1])

    l = len(divelogs)
    for i in range(0, l):
        average_depth(divelogs[l - i - 1])

def average_depth(divelogID):
    # if len(sys.argv)==2:
    #     divelogID = sys.argv[1]
    # result = deepblu_api.get_divelog(divelogID)
    # print(result)
    # dict = {}
    # temp = {}
    # dict = result
    dict = divelogID
    print('DivelogId: %s' % divelogID['_id'])
    print('DiveType: %s' % divelogID['diveType'])
    divelog = []


    divetime=str(dict['diveDTRaw']).split(',')
    print("divetime: %s/%s/%s %s:%s" % (divetime[0],divetime[1],divetime[2],divetime[3],divetime[4]))


    # Max Depth

    # airPressure 沒有值得話 設定1000
    airPressure=0
    if ('airPressure' in dict):
        airPressure = dict['airPressure']
        print(airPressure)
    else:
        airPressure = 1000

    watertype = 0
    if ('waterType' in dict):
        if dict['waterType'] == 1:
            watertype = 102.5
        else:
            watertype = 100

    else:
        watertype = 100

    print(airPressure,watertype,dict['diveMaxDepth'])
    max_depth = (dict['diveMaxDepth']-airPressure)/float(watertype)
    max_depth_ft = max_depth *ft
    print('Max Dapth: %s m'% max_depth)
    max_depth = round(max_depth*10)/10
    # max_depth = float(str(round(max_depth,2))[:-1])

    print("Max Depth: %s m / %sft"% (max_depth,round(max_depth_ft)))

    # 0:淡水->100 預設是淡水
    # 1:鹹水-->102.5

    if('waterType' in dict):
     if dict['waterType']==1:
        watertype=102.5
     else:
        watertype=100

    else:
        watertype=100

    # print("watertype:" + str(watertype))


    #airPressure 沒有值得話 設定1000
    if('airPressure' in dict):
        airPressure=dict['airPressure']
    else:
        airPressure=1000

    # print("airPressure:" + str(airPressure))
    diveProfile={}
    diveProfile=dict['_diveProfile']
    allprofile=len(diveProfile)
    # print("allprofile:"+str(allprofile))

    for items in range(0,allprofile):
        temp=diveProfile[items]
        divelog.append(temp['pressure'])
        depth = (temp['pressure'] - airPressure)/watertype
        # print("%.2f m" % (depth))

    # print('-' * 20)
    for items in range(0, allprofile):
        temp = diveProfile[items]
        depth = (temp['pressure'] - airPressure) / watertype
        # print("%.2f ft" % (depth*ft))


    # print(divelog)
    # print("Total is "+ str(sum(divelog)))

    # [(logDive._diveProfile.pressure 加總 ÷ profile總數) - air pressure] / waterType
    average=((sum(divelog)/allprofile)-airPressure)/float(watertype)
    # average=round(sum(divelog)/allprofile,1)
    # print("sum(divelog)/allprofile:"+str(sum(divelog)/allprofile))
    # average=(average-airPressure)/watertype
    print("average: %.1f m, %f m" % (round(average,1),average))
    print("average: %.1f m, %f m" % (average, average))
    print("average: %.1f ft, %f ft" % (round(average*ft,2),average*ft))


    # duration
    duration = dict['diveDuration']
    hour=0
    min = 0
    if duration > 3600:
        hour="01"
        min = round((duration-3600)/60)
    else:
        hour ="00"
        min = round(duration/60)

    print("duration: %s:%s / %s seconds" %(hour,min,duration))
    print('======================\n')

if __name__ == "__main__":
    get_raw_divelog('hi@deepblu.com')
