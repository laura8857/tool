# -*- coding: utf-8 -*-

from pymongo import *

#remove raw divelog
def remove_raw_divelog(email):
    # connect to mongo
    client = MongoClient("52.197.14.177", 27017)
    client.deepblu.authenticate('deepblu2', 'DGeANYhWyx8prMFgYEj6', mechanism='MONGODB-CR')
    db = client.deepblu

    if db.user.find_one({"email": email}):
        user = {}
        token = ""
        user = db.user.find_one({"email": email})
        id = user['_id']
        #print(str(id))

        count = db.LogDive.find({"ownerId":id,"status":"Raw"}).count()
        if count >0:
            db.LogDive.remove({"ownerId":id,"status":"Raw"})
            print(str(count)+" raw logs are removed.")
        else:
            print("There is no raw log.")
    else:
        print("The mail " + email + " can't be found.")
    client.close()

#count raw dive log
def raw_divelog_count(email):
    # connect to mongo
    client = MongoClient("52.197.14.177", 27017)
    client.deepblu.authenticate('deepblu2', 'DGeANYhWyx8prMFgYEj6', mechanism='MONGODB-CR')
    db = client.deepblu

    if db.user.find_one({"email": email}):
        user = {}
        token = ""
        user = db.user.find_one({"email": email})
        id = user['_id']
        #print(str(id))

        if db.LogDive.find({"ownerId":id,"status":"Raw"}).count()>0:
            print("Raw log count:"+str(db.LogDive.find({"ownerId":id,"status":"Raw"}).count()))
        else:
            print("There is no raw log.")
    else:
        print("The mail " + email + " can't be found.")
    client.close()

if __name__ == "__main__":
    # raw_divelog_count("alex@deepblu.com")
    remove_raw_divelog("hice@deepblu.com")

