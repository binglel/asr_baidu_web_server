# encoding: utf-8
# ******************************************************
# requirement:python3
# Author: chyb
# Last modified: 20190920_10:30
# Email: chyb3.14@gmail.com
# Filename:
# Description: 客户端
# ******************************************************
import json
import base64
import requests


file = "./data/recording.wav"
file_type = file[-3:]
data_bytes = open(file,"rb").read()
data_str = base64.b64encode(data_bytes).decode("utf-8")
print (file_type)
print (data_str)
response = requests.post("http://10.3.27.93:8080/asr", json=dict(type=file_type,data=data_str))
if response.status_code == 200:
    print(response.text)



