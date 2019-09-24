#!/bin/env python

from flask import *
from accounts import AccountResource
import json


app = Flask(__name__)
res = AccountResource()


@app.route('/api/accounts/', methods=['GET'])
def list_accounts():
    return json.dumps(res.get_accounts())


@app.route('/api/accounts/<int:accid>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def account(accid):
    if request.method == 'GET':
        acc = res.get_account_by_id(accid)
        return json.dumps(res.get_account_by_id(accid))
    if request.method == 'PUT':
        pass
    if request.method == 'POST':
        pass
    if request.method == 'DELETE':
        pass


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)