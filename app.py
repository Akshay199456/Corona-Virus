import os
import json
import requests

from flask import Flask
from flask import jsonify, make_response


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config.from_object(os.environ['APP_SETTINGS'])

print(os.environ['APP_SETTINGS'])

@app.route('/')
def home():
	return 'Hello World!'

@app.route('/states')
def hello():
	response = requests.get('https://covidtracking.com/api/states')
	if response:
		print('Response: ', response)
		# json.loads takes in a string and returns a json object
		json_object = json.loads(response.text)
		# The jsonify() function in flask returns a flask.Response() object 
		# that already has the appropriate content-type header 'application/json' 
		# for use with json responses. Whereas, the json.dumps() method will just return 
		# an encoded string, which would require manually adding the MIME type header.
		return jsonify(json_object)
	else:
		print('Error occurred!')
		return "Error"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run()