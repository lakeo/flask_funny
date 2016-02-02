# -*- coding: utf-8 -*-

from flask import render_template
from funny import funny
from flask import jsonify

from controllers import JokeController

@funny.route('/')
def index():
    jokes = JokeController.getLatestJokes()
    jokes = jokes if jokes else []
    index = 1000000000
    if jokes:
        index = jokes[-1]['id']
    return render_template('index.html',jokes=jokes,index=index)

@funny.route('/about.html')
def about():
    return render_template('about.html')

@funny.route('/api/jokes/<index>')
def getJokes(index):
    jokes = JokeController.getJokes(index)
    ret = {"data":jokes}
    return jsonify(ret)
