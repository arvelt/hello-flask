# coding: utf-8

import sys, os, pytest
sys.path.append(os.path.abspath('./'))
import main
from flask import jsonify

def test_get_root():
    app = main.app.test_client()
    print res.status
    assert res.status == '200 OK'
    assert res.data == 'Hello World!'

def test_get_data():
    app = main.app.test_client()
    res = app.get('/data')
    assert res.status == '200 OK'
    assert res == jsonify(result='Hello Workd!')
