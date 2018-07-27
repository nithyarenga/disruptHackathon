from bottle import route, run
from bottle import post, get, put, delete
from bottle import response, request
from json import dumps, loads

@get('/hello')
def hello():
    return "Hello World!"

@post('/images')
def images():
        value = request.body.read()
        v = loads(value)
        print v['user_id']
        print v['url']
        response.status = 200
        return {}

run(host='172.30.0.165', port=8089, debug=True)
