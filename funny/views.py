# -*- coding: utf-8 -*-

from flask import render_template
from funny import funny
from flask import jsonify
from flask import request
from flask import redirect,url_for
import random

from controllers import JokeController


#user view
import view.user

@funny.route('/')
def index():
    random = request.args.get('r','')
    if random:
        jokes = JokeController.getJokes(random)
    else:
        jokes = JokeController.getLatestJokes()
    jokes = jokes if jokes else []
    index = 1000000000
    if jokes:
        index = jokes[-1]['id']
    return render_template('index.html',jokes=jokes,index=index)

@funny.route('/random.html')
def goRandom():
    joke = JokeController.getRandomJoke()
    seed = joke['id']
    return redirect(url_for('index',r=seed))

@funny.route('/about.html')
def about():
    return render_template('about.html')


@funny.route('/api/jokes/<index>')
def getJokes(index):
    jokes = JokeController.getJokes(index)
    ret = {"data":jokes}
    return jsonify(ret)
