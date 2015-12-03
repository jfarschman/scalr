#!/usr/bin/python
#coding:utf-8
""" - FarmGetDetails.py

`FarmGetDetails.py` retrieves some of the details about a farm in Scalr
using their API. 

You will need to setup environment variables specific to your install
installation.  For example

	export SCALR_API_KEY=YOUR_API_KEY
	export SCALR_SECRET_KEY=YOUR_SECRET_KEY
	export SCALR_API_URL=YOUR_API_ENDPOINT

Syntax:
	./FarmGetDetails.py <farm_id>

"""
__author__ = "Jay Farschman"
__license__ = "GPL"
__version__ = "0.1.0"
__maintainer__ = "Jay Farschman"
__email__ = "jfarschman@gmail.com"
__status__ = "Development"

import datetime
import urllib
import base64
import hmac
import hashlib
import os
import sys
import xml.dom.minidom

""" Import variables """
farm_id = str(sys.argv[1])

""" Connect to the API """
SCALR_API_KEY = os.environ["SCALR_API_KEY"]
SCALR_SECRET_KEY = os.environ["SCALR_SECRET_KEY"]
SCALR_API_URL = os.environ["SCALR_API_URL"]

API_VERSION = '2.3.0'
API_AUTH_VERSION =  '3'

API_ACTION = "FarmGetDetails"


def main(key_id, secret_key):
    timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

    params = {
        "Action": API_ACTION,
        "Version": API_VERSION,
        "AuthVersion": API_AUTH_VERSION,
        "Timestamp": timestamp,
        "KeyID": key_id,
        "FarmID": farm_id,
        "Signature":  base64.b64encode(hmac.new(secret_key, ":".join([API_ACTION, key_id, timestamp]), hashlib.sha256).digest()),
    }

    urlparams = urllib.urlencode(params)
    req = urllib.urlopen(SCALR_API_URL, urlparams)

    return req.read()

if __name__ == "__main__":
    s=main(SCALR_API_KEY, SCALR_SECRET_KEY)
    print xml.dom.minidom.parseString(s).toprettyxml()
