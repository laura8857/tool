# -*- coding: utf-8 -*-
#刪除該帳號的terms&conditions

import pymysql
from pymongo import MongoClient


def remove_terms_conditions(email):
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

    #connect mysql db
    db = pymysql.connect(host='52.197.14.177',user='root',passwd='54353297',db='test',port=3306,charset='utf8')
    cursor = db.cursor()

    sql = "DELETE FROM deepblu.SignCondition WHERE userId='"+id+"'"

    try:
        cursor.execute(sql)
        db.commit()
        print('Succuss')
    except:
        print('Error')
    db.close()

if __name__ == "__main__":
    remove_terms_conditions('laura@deepblu.com')