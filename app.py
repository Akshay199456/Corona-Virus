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
def hello():
	response = requests.get('https://covidtracking.com/api/states')
	if response:
		print('Response: ', response)
		json_object = json.loads(response.text)
		return json.dumps(json_object, indent=2)
	else:
		print('Error occurred!')
		return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run()