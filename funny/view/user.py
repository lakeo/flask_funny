# -*- coding: utf-8 -*-

from flask import render_template
from funny import funny
from flask import request

@funny.route('/user/login.html', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')


@funny.route('/user/register.html', methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')


@funny.route('/user/findPassword.html')
#todo
def findPassword():
    pass


@funny.route('/user/changePassword')
#todo
def changePassword():
    pass
