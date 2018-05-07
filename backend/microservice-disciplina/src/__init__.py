import os
from flask import Flask

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)
app.secret_key = 'E1C2C311C75BBCC222E9E9D61A64134EB19C869020681FAE7BCF5D8FD4796F70'
app.debug = os.getenv('FLASK_DEBUG', False)

import src.app