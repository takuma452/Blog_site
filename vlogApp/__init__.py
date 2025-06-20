from flask import Flask

app = Flask(__name__)
app.config.from_object('vlogApp.config')

import vlogApp.views