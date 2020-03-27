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


@app.route('/api/<state>')
def api(state):
	'''
	Getting data from http://coronavirusapi.com/
	'''
	response = requests.get('http://coronavirusapi.com/getTimeSeries/' + state)
	if response:
		print('Response from api: ', response)
		# Data returned from api in 'str' format
		text_response = json.dumps(response.text)
		print('Response text from api: ', text_response)
		if(text_response == '"Please use a 2 letter state abbreviation"'):
			return 'Invalid State'
		else:
			# Tokenize the data
			all_data = response.text.split('\n')
			print('All data: ', all_data)
			return 'State: ' + state
	else:
		print('Error occurred!')
		return "Error"



@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run()