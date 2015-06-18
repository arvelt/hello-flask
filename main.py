from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/data")
def get_data():
    print jsonify({1:1})
    return jsonify(result='Hello Workd!')

if __name__ == "__main__":
    app.run()
