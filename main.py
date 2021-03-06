from flask import Flask, jsonify, make_response, request, render_template
app = Flask(__name__)

@app.route("/")
def hello():
	template = u"""
	<!DOCTYPE html>
	<html>
	<body>
		Hello world!
		<ul>
		<li><a href="/http_method">Http method</a></li>
		<li><a href="/json_data">Json data</a></li>
		<li><a href="/static_files">Static files</a></li>
		<li><a href="/using_templates">Using templates</a></li>
		</ul>
	</body>
	</html>
	""".strip()
	response = make_response(template)
	return response

@app.route('/using_templates/')
@app.route('/using_templates/<name>')
def using_templates(name=None):
	return render_template('welcome.html', name=name)

@app.route("/static_files")
def static_files():
	template = u"""
	<!DOCTYPE html>
	<html>
	<head>
		<link rel="stylesheet" href="/static/style.css" type="text/css">
	</head>
	<body>
		<div class="red">Using style</div>
	</body>
	</html>
	""".strip()
	response = make_response(template)
	return response

@app.route("/http_method", methods=['GET', 'POST'])
def http_method():
	if request.method == 'POST':
		return "POST is received."
	else:
		template = u"""
		<!DOCTYPE html>
		<html>
		<body>
			GET is received.
			<form method="POST">
				<input type="submit" value="request POST metohd">
			</form
		</body>
		</html>
		""".strip()
		response = make_response(template)
		response.headers['X-Parachutes'] = 'parachutes are cool'
		return response

@app.route("/json_data")
def json_data():
    res = {'result': 'Hello World!'}
    return jsonify(res)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
