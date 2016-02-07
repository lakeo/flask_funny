# -*- coding: utf-8 -*-

from flask.ext.login import login_user

from funny.tools import PasswordTool
from funny.model.user import User
import logging

class UserController(object):
    @classmethod
    def registerByEmail(cls,email,password):
        passwordhash = PasswordTool.createPasswordHash(password)
        ret = User.registerByEmail(email,passwordhash)
        logging.info('register user: %s, %s, %s',str(ret),email,passwordhash)
        return ret

    @classmethod
    def loginByEmail(cls,email,password):
        user = User.getUserByEmail(email)
        if not user:
            return '用户不存在'
        passwordhash = user['password']
        logging.info(passwordhash)
        ret = PasswordTool.validatePassword(password,passwordhash)
        if ret:
            login_user(user)
            return user
        else:
            return '密码不正确'
