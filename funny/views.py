# -*- coding: utf-8 -*-

from flask import render_template
from funny import funny
from flask import jsonify
from flask import request
from flask import redirect,url_for
from flask.ext.login import current_user

from funny.controller.jokeController import JokeController

#user view
import view.user
@funny.route('/')
@funny.route('/index.html')
def index():
    random = request.args.get('r','')
    jokes = JokeController.getLatestJokes(current_user)
    jokes = jokes if jokes else []
    index = 1000000000
    if jokes:
        index = jokes[-1]['id']
    return render_template('index.html',jokes=jokes,index=index)

@funny.route('/random.html')
def goRandom():
    joke = JokeController.getRandomJoke()
    random = joke['id']
    jokes = JokeController.getJokes(current_user,random)
    jokes = jokes if jokes else []
    index = 1000000000
    if jokes:
        index = jokes[-1]['id']
    return render_template('random.html',jokes=jokes,index=index)

@funny.route('/article/joke/<id>')
def getJoke(id):
    joke = JokeController.getJoke(id,current_user)
    return render_template('article.html',joke=joke)

@funny.route('/about.html')
def about():
    return render_template('about.html')


@funny.route('/api/jokes/<index>')
def getJokes(index):
    jokes = JokeController.getJokes(current_user,index)
    ret = {"data":jokes}
    return jsonify(ret)

@funny.route('/api/like/article/<id>')
def likeArticle(id):
    ret = {}
    if not current_user.is_authenticated():
        ret['error'] = {'info':'no login'}
        return jsonify(ret)
    userid = current_user.get_id()

    flag,value = JokeController.likeJoke(id,userid)
    if flag:
        ret['success']=1
        ret['info'] = value
    else:
        ret['success']=0
        ret['info'] = value
    return jsonify(ret)
