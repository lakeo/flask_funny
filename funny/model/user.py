# -*- coding: utf-8 -*-

from flask.ext.login import UserMixin
import SimpleDB
import funny.config
import time
import logging

from funny.environ import login_manager

def getDB():
    return SimpleDB.MySQLdb(
                host='localhost',
                port = 3306,
                user='joke',
                passwd='joke',
                db ='joke',
                use_unicode=True,
                charset='utf8')

class User(UserMixin):
    '''
    userid
    email
    password
    create time
    update time
    create ip
    phone
    validated 是否验证过
    还有一些没有考虑到的,暂时不记录在数据库中,先记录在log中,周期性备份,以备日后使用
    '''
    _user = {}
    id = 0
    def __init__(self,data):
        self._user  = data
        self.id = int(data['userid'])
        logging.info(self.id)

    def getUserName(self):
        if 'name' in self._user:
            return self._user['name']
        return self._user['email']

    def __getitem__(self,name):
        if name in self._user:
            return self._user[name]
        raise NotImplementedError('There is not attribute %s' % name )

    @classmethod
    def registerByEmail(cls,email,password):
        db = getDB()
        sql = 'insert into user(email,password,ctime,utime) values(%s,%s,%s,%s)'
        ret = ''
        try:
            db.insert(sql,email,password,int(time.time()),int(time.time()))
        except Exception,e:
            logging.info('register error: %s',e)
            ret = '该email已经被注册过了'
        return ret

    @classmethod
    def getUserByEmail(cls,email):
        db = getDB()
        sql = 'select userid, email, password from user where email=%s'
        ret = {}
        try:
            ret = db.query_dict_row(sql,email)
            ret = User(ret)
        except Exception,e:
            logging.warn('in getUserByEmail %s', e)
        return ret

    @classmethod
    def getUserByUserid(cls,userid):
        db = getDB()
        sql = 'select userid, email, password from user where userid=%s'
        ret = {}
        try:
            ret = db.query_dict_row(sql,userid)
            ret = User(ret)
        except Exception,e:
            logging.warn('in getUserByEmail %s', e)
        return ret

@login_manager.user_loader
def load_user(userid):
    return User.getUserByUserid(userid)
