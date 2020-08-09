# -*- coding: utf-8 -*-
"""
Created on Mon May 18 09:41:47 2020

@author: Delta
"""




from ppadb.client import Client
import time

# Default is "127.0.0.1" and 5037
adb = Client(host="127.0.0.1", port=5037)

devices = adb.devices()
device = devices[0]

while True:
     device.shell('input touchscreen tap 523 1301')
     time.sleep(0.48)