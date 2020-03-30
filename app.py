import os

import main

from flask import Flask


def create_app(test_config=None):
	# create and configure the app
	app = Flask(__name__, instance_relative_config=True)
	app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
	app.config.from_object(os.environ['APP_SETTINGS'])
	print('OS Environment: ', os.environ['APP_SETTINGS'])
	if test_config is None:
		# load the instance config, if it exists, when not testing
		app.config.from_pyfile('config.py', silent=True)
	else:
		# load the test config if passed in
		app.config.from_mapping(test_config)

	# ensure the instance folder exists
	try:
		os.makedirs(app.instance_path)
	except OSError:
		pass

	app.register_blueprint(main.bp)
	return app

if __name__ == '__main__':
	create_app().run()