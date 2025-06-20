from flask import Flask

app = Flask(__name__)
app.config.from_objevt('vlogapp.config')

import vlogApp.views