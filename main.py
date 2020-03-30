import json
import requests
import pandas as pd

from flask import Flask, jsonify, make_response, Blueprint

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def home():
	return 'Hello World!'

@bp.route('/states')
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


@bp.route('/api/<state>')
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
			# Get the column names
			column_names = all_data[0].split(',')
			# Get the actual data
			datapoints = []
			for element in all_data[1:]:
				datapoints.append([0 if x=='' else int(x) for x in element.split(',')])

			print('Column names: ', column_names)
			print('Data points: ', datapoints)


			# df = pd.DataFrame({"Name": ["Braund, Mr. Owen Harris","Allen, Mr. William Henry","Bonnell, Miss. Elizabeth"],"Age": [22, 35, 58],"Sex": ["male", "male", "female"]})
			# print('Pandas df: ', df)
			return 'State: ' + state
	else:
		print('Error occurred!')
		return "Error"



@bp.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)