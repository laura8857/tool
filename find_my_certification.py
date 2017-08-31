# -*- coding: utf-8 -*-
# 刪除該帳號的terms&conditions

import pymysql
from pymongo import MongoClient


def find_my_certification(email):
    # connect to mongo
    client = MongoClient("52.197.14.177", 27017)
    client.deepblu.authenticate('deepblu2', 'DGeANYhWyx8prMFgYEj6', mechanism='MONGODB-CR')
    db = client.deepblu

    if db.user.find_one({"email": email}):
        user = {}
        token = ""
        user = db.user.find_one({"email": email})
        id = str(user['_id'])
        # print(str(id))

    else:
        print("The mail " + email + " can't be found.")
    client.close()

    # connect mysql db
    db = pymysql.connect(host='52.197.14.177', user='root', passwd='54353297', db='test', port=3306, charset='utf8')
    # 獲取一個游標
    cursor = db.cursor()

    sql = "SELECT organizationName,certificationLevel,organizationRank,certificationRank,issueStatus FROM " \
          "deepblu.DiverCertification as a, deepblu.DiveCertificationMeta as b " \
          "where a.ownerId = '" + id + "' AND a.certificationMetaId = b.id "
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        print('Succuss')
        # print(results)

        list = []
        if len(results) > 0:
            for item in results:
                if item[4] == 'active':
                    status = 1
                else:
                    status = 0
                list.append({
                    'status': status,
                    'orgLvl': item[2],
                    'certiLvl': item[3],
                    'orgName': item[0],
                    'certiName': item[1],
                })
            # print(list)

        final = []


        if len(list) > 1:

            final = list[0]
            # 比較active or not 取分數大
            # 比較certification level 取分數大
            # 比較 organization level 取分數小
            for i in range(1, len(list)):
                # print(i)
                if list[i]['status'] == final['status']:
                    if list[i]['certiLvl'] > final['certiLvl']:
                        final = list[i]
                    elif list[i]['certiLvl'] == final['certiLvl']:
                        if list[i]['orgLvl'] < final['orgLvl']:
                            final = list[i]
                elif list[i]['status'] > final['status']:
                    final = list[i]
                else:
                    pass

            print(final['orgName'], final['certiName'])
        elif len(list) == 0:
            print('There is no certification')
        else:
            final = list[0]
            print(final['orgName'], final['certiName'])

    except:
        print('Error')
    # 關閉游標
    cursor.close()
    # disconnect db
    db.close()


if __name__ == "__main__":
    find_my_certification('laura4@deepblu.com')
