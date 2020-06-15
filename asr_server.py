# encoding: utf-8
# ******************************************************
# requirement:python3
# Author: chyb
# Last modified: 20190920_10:30
# Email: chyb3.14@gmail.com
# Filename:
# Description: asr web server based on falsk
# ******************************************************

from flask import Flask
from asr import asr_api
from flask import request
from baidu_token import TOKEN
import traceback
app = Flask(__name__)

@app.route('/asr', methods=['POST'])
def asr_server():
    try:
        # data_params = dict(type= request.args['type'], data=request.data)
        params = request.form if request.form else request.json
        type = params.get("type","")
        data = params.get("data","")
        data_params = dict(type=type, data=data)
        result = asr_api(data_params, TOKEN)
        print (result)
    except Exception as e:
        traceback.print_exc()
        return "err: %s" % e.message
    else:
        return result

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=8080, debug=True)
    # app.run(host='127.0.0.1', port=8080, debug=True)
    app.run(host='10.3.27.93', port=8080, debug=True)