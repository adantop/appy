#!/bin/env python

from flask import request, Flask, render_template, make_response, redirect

app = Flask(__name__)


USERS = {
    'adant': 'potato',
    'pooya': 'tomato'
}

@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/hello')
def hello(user='default'):
    user = request.cookies.get('user', '')
    pawd = request.cookies.get('pawd', '')
    return render_template('hello.html', user=user)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form.get('user', '')
        pawd = request.form.get('pawd', '')
        if USERS.get(user) == pawd:
            resp = make_response(redirect('/hello'))
            resp.set_cookie('user', user)
            resp.set_cookie('pawd', pawd)
            return resp
        else:
            return render_template('login.html', user=user, pawd=pawd)
    elif request.method == 'GET':
        return render_template('login.html', user='', pawd='')


@app.route('/logout', methods=['POST', 'GET'])
def logout():
        resp = make_response(render_template('logout.html'))
        resp.set_cookie('user', '', expires=0)
        resp.set_cookie('pawd', '', expires=0)
        return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
