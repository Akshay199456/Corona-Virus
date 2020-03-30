import os

import main

from flask import Flask


# create and configure the app
app = Flask(__name__, instance_relative_config=True)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config.from_object(os.environ['APP_SETTINGS'])
print('OS Environment: ', os.environ['APP_SETTINGS'])

app.register_blueprint(main.bp)

if __name__ == '__main__':
	app.run()