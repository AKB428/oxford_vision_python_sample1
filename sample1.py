########### Python 2.7 #############
import httplib, urllib, base64
import sys

import json
f = open('./config/application.json', 'r')
config = json.load(f)
f.close()

headers = {
    # Request headers
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': config['Azure']['subscription_key'],
}

params = urllib.urlencode({
    # Request parameters
    'visualFeatures': 'All',
})

try:
    argv = sys.argv
    data = open(argv[1], "r+b").read()
    conn = httplib.HTTPSConnection('api.projectoxford.ai')
    conn.request("POST", "/vision/v1/analyses?visualFeatures=All", data, headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
