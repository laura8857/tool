# -*- coding: utf-8 -*-
# @Time    : 2017/4/14 下午6:34
# @Author  : Yuhsuan
# @File    : group_summary_notification.py
# @Software: PyCharm Community Edition

from pymongo import *
from datetime import datetime
import pymysql

def group_summary_notification(email):
    #Create Connection
    client = MongoClient("52.197.14.177", 27017)
    client.deepblu.authenticate('deepblu2', 'DGeANYhWyx8prMFgYEj6', mechanism='MONGODB-CR')
    db = client.deepblu

    if db.user.find_one({"email": email}):
        ownerid=db.user.find_one({"email": email})['_id']

        # timezone
        utc = datetime.utcnow().hour
        if int(datetime.utcnow().minute) >=30:
            print(datetime.utcnow().minute)
            utc = utc+1
        set_time = 12-utc
        if set_time >=10:
            set_time = "+"+str(set_time)+"00"
        elif set_time >=0:
            set_time = "+0"+str(set_time)+"00"
        elif set_time >=-9:
            set_time = "-0"+str(-1*set_time)+"00"
        else:
            set_time = str(set_time)+"00"

        print("timezone: "+set_time)

        print("original: ", db.duser.find_one({"ownerId":ownerid},{"timeZone":1}))
        db.duser.update_one({"ownerId":ownerid}, {"$set": {"timeZone": set_time}})
        print("changed: ", db.duser.find_one({"ownerId": ownerid}, {"timeZone": 1}))
        update_sql(str(ownerid))
    else:
        print("The mail " + email + " can't be found.")
    client.close()
    print("\nmongo update done")

def update_sql(ownerId):
    conn = pymysql.connect(host="52.197.14.177", port=3306, user="root", passwd="54353297", db="deepblu",
                           charset="UTF8")
    try:
        with conn.cursor() as cur:
            sql = "SELECT * FROM deepblu.GroupVisitTime where userId='"+ownerId+"';"
            sql_update = "UPDATE deepblu.GroupVisitTime SET visitTime='2017-04-01 12:00:00' WHERE userId='"+ownerId+"';"
            cur.execute(sql_update)
            # print(cur.fetchall())
            conn.commit()

            cur.execute(sql)
            result = cur.fetchall()
            print("\nMysql Result:")
            for row in result:
                groupid = row[0]
                userid = row[1]
                visittime = row[2]
                createtime = row[3]
                updatetime = row[4]
                print(groupid,userid,visittime,createtime,updatetime)

    except Exception as e:
        print(e)
    finally:
        conn.close()
        print("\nmysql update done")

if __name__=="__main__":
    group_summary_notification("101403032@cc.ncu.edu.tw")

#101403032@cc.ncu.edu.tw