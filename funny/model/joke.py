# -*- coding: utf-8 -*-

from funny.tools.mysql import getDB
from funny.constants import JOKE_TYPE
import logging


class Joke(object):
    @classmethod
    def getRandomJoke(cls, seed):
        db = getDB()
        sql = 'select * from joke where rand() < %s order by id desc limit 1'
        joke = db.query_dict_row(sql, seed)
        return joke

    @classmethod
    def getJokesList(cls, begin, limit):
        db = getDB()
        sql = 'select * from joke WHERE id < %s order by id desc limit %s'
        jokes = db.query_dict(sql, begin, limit)()
        return jokes

    @classmethod
    def getLatestJokesList(cls, steps):
        db = getDB()
        sql = 'select * from joke order by id desc limit %s'
        jokes = db.query_dict(sql, steps)()
        return jokes

    @classmethod
    def getTotal(cls):
        db = getDB()
        sql = 'select count(1) from joke'
        return db.query_tuple_row(sql)[0]

    @classmethod
    def getJoke(cls, id):
        db = getDB()
        sql = 'select * from joke where id = %s'
        joke = db.query_dict_row(sql, id)
        return joke

    @classmethod
    def likeJoke(cls, jokeid, userid):
        db = getDB()
        sql = 'select type from article_like where userid=%s and article_id = %s and article_type=%s'
        type = db.query_tuple_row(sql, userid, jokeid, JOKE_TYPE)

        if type and type[0] <= 0:
            newType = -1
        else:
            newType = 1

        sql = 'insert article_like (userid,article_id,article_type,type,ctime,utime) values (%s,%s,%s,%s,UNIX_TIMESTAMP(),UNIX_TIMESTAMP()) on duplicate key update type=%s,utime=UNIX_TIMESTAMP()'
        db.insert(sql, userid, jokeid, JOKE_TYPE, newType, newType)

        if not type and newType == 1:
            sql = 'update joke set like_number = like_number + %s where id = %s'
            ret = db.update(sql, newType, jokeid)
        else:
            sql = 'update joke set like_number= like_number + %s where id = %s'
            ret = db.update(sql, newType, jokeid)
        return (True,newType)

    @classmethod
    def getLikeStatus(cls,jokeid,userid):
        db = getDB()
        sql = 'select type from article_like where article_id = %s and userid=%s and article_type=%s'
        ret= db.query_tuple_row(sql,jokeid,userid,JOKE_TYPE)
        if not ret or int(ret[0]) != 1:
            return False
        else:
            return True
