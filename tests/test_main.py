# coding: utf-8

import sys, os, pytest
sys.path.append(os.path.abspath('./'))
import main
import json


def test_get_root():
    app = main.app.test_client()
    res = app.get('/')
    assert res.status == '200 OK'
    assert res.data == 'Hello World!'

def test_get_data():
    app = main.app.test_client()
    res = app.get('/data')
    assert res.status == '200 OK'
    expect = json.dumps({'result':'Hello World!'})
    print expect
    assert res.data.replace('\n', '').replace(' ','') == expect.replace(' ','')
