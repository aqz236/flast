# -*- coding: UTF-8 -*-
# app.py
from flask import Flask
from utils.config import ConfigUtil
from utils.route_manager import RouteManager

config = ConfigUtil().get_config()['flask']
app = Flask(__name__)
RouteManager(app)

if __name__ == "__main__":
    app.run(
        host=config['host'],
        port=config['port'],
        debug=True
    )
