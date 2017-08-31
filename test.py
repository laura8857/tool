# -*- coding: utf-8 -*-

from flask import Flask
import gevent.pywsgi
import gevent
import datetime
app = Flask(__name__)
@app.route('/')
def handle():
    total = 9
    now = datetime.datetime.now()
    d1 = datetime.datetime(2016,12,31)
    day = (now - d1).days
    rate = float(day)/365

    rest_hr = total * rate * 8
    rest_day = rest_hr/8

    # print('Rest hour :%.2f,rest day: %.2f'% (rest_hr,rest_day))
    return 'Rest hour :%.2f hr \n Rest day: %.2f days'% (rest_hr,rest_day)
gevent_server = gevent.pywsgi.WSGIServer(('', 5000), app)
gevent_server.serve_forever()


# if __name__ == "__main__":
#     handle()