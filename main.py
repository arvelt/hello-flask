from flask import Flask, jsonify
from flask import make_response
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/raw_response")
def get():
    template = u"""
    <!DOCTYPE html>
    <html>
    <body>
        Raw string template.
    </body>
    </html>
    """
    response = make_response(template)
    response.headers['X-Parachutes'] = 'parachutes are cool'
    return response

@app.route("/data")
def get_data():
    res = {'result': 'Hello World!'}
    return jsonify(res)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
