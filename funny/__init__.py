# -*- coding: utf-8 -*-

from flask import Flask, url_for
import os

funny = Flask(__name__)

# Determines the destination of the build. Only usefull if you're using Frozen-Flask
funny.config['FREEZER_DESTINATION'] = os.path.dirname(os.path.abspath(__file__))+'/../build'

# Function to easily find your assets
# In your template use <link rel=stylesheet href="{{ static('filename') }}">
funny.jinja_env.globals['static'] = (
    lambda filename: url_for('static', filename = filename)
)

import environ
import config

from funny import views
