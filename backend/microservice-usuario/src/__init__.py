import os
from flask import Flask

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)
app.secret_key = 'DDB0AD550D489065F36B764150B5156576D892A32589E35871B671B66546BAC0'
app.debug = os.getenv('FLASK_DEBUG', False)

import src.app