# -*- coding: utf-8 -*-

# 2017-01-20 by Yuhsuan
# Default test device is iPhone 5s with ios 9.3
# If we need to test browser, need to disable app and add browser in desired_capabilities.

import os
import datetime

directory = '%s/' % os.getcwd()

def get_desired_capabilities(test_type, app_path):

    # desired_caps['browserName'] = 'safari'
    # desired_caps['app'] = directory+'DeepbluApp_2.0.0_adhoc.ipa'
    # desired_caps['bundleId'] = 'com.deepblu.deepblu'

    desired_caps = {
        'deviceName': 'iPhone 5s',
        'platformName': 'iOS',
        'platformVersion': '9.3',
    }

    if test_type == 'app':
        if app_path=='Settings':
            desired_caps['app'] = app_path
        else:
            # Need to install app
            desired_caps['app'] = directory + app_path

    elif test_type == 'bundleId':
        # Know bundle id
        desired_caps['bundleId'] = app_path

    elif test_type == 'browser':
        # Test browser
        desired_caps['browserName'] = 'safari'
    else:
        # Default is using com.deepblu.deepblu
        desired_caps['bundleId'] = 'com.deepblu.deepblu'

    return desired_caps