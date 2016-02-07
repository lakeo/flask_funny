# -*- coding: utf-8 -*-

from flask import flash,render_template
from flask import request,session
from flask import redirect,url_for
from flask.ext.login import current_user,logout_user

import logging

from funny import funny
from funny.controller.UserController import UserController

@funny.route('/user/login.html', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        hint = request.args.get('hint','')
        if hint:
            flash(hint)
        return render_template('login.html')

    #已经登录的不需要再登录
    if current_user.is_authenticated():
        return redirect('/')

    email = request.form['email']
    password = request.form['password']

    if not email or not password:
        flash('用户名或密码不能为空.')
        return render_template('login.html')

    ret = UserController.loginByEmail(email,password)
    if isinstance(ret,str):
        logging.info('user login fail email=%s %s',email,ret)
        flash('用户名或者密码错误')
        return render_template('login.html')

    logging.info('user login id=%s',current_user.id)
    return redirect('/')


@funny.route('/user/register.html', methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    email = request.form['email']
    password = request.form['password']

    if not email or not password:
        flash('输入数据不能为空')
        return render_template('register.html')

    error = UserController.registerByEmail(email,password)
    if not error:
        return redirect(url_for('login',hint='注册成功,请登录.'))
    else:
        flash(error)
        return render_template('register.html')

@funny.route('/user/findPassword.html')
#todo
def findPassword():
    pass

@funny.route('/user/changePassword')
#todo
def changePassword():
    pass

@funny.route('/user/logout.html')
#todo
def logout():
    logging.info('user logout id=%s',current_user.id)
    logout_user()
    return redirect('/')
