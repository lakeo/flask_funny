# -*- coding: utf-8 -*-

import SimpleDB
import config
import time
import logging

def getDB():
    return SimpleDB.MySQLdb(
                host='localhost',
                port = 3306,
                user='joke',
                passwd='joke',
                db ='joke',
                use_unicode=True,
                charset='utf8')


class Joke(object):
    @classmethod
    def getRandomJoke(cls,seed):
        db = getDB()
        sql = 'select * from joke where rand() < %s order by id desc limit 1'
        joke = db.query_dict_row(sql, seed)
        return joke

    @classmethod
    def getJokesList(cls,begin,limit):
        db = getDB()
        sql = 'select * from joke WHERE images ="" and id < %s order by id desc limit %s'
        jokes = db.query_dict(sql,begin,limit)()
        return jokes

    @classmethod
    def getLatestJokesList(cls, steps):
        db = getDB()
        sql = 'select * from joke where images = "" order by id desc limit %s'
        jokes = db.query_dict(sql,steps)()
        return jokes

    @classmethod
    def getTotal(cls):
        db = getDB()
        sql = 'select count(1) from joke'
        return db.query_tuple_row(sql)[0]
