from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/data")
def get_data():
    res = {'result': 'Hello World!'}
    return jsonify(res)

if __name__ == "__main__":
    app.run()
