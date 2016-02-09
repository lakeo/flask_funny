# -*- coding: utf-8 -*-
from funny.model.joke import Joke

class JokeController(object):
    @classmethod
    def getJokes(cls,user,index=10000000,step=10):
        jokes = Joke.getJokesList(index,step)
        ret = []
        for joke in jokes:
            if user.is_authenticated():
                like = Joke.getLikeStatus(joke['id'],user.id)
                joke['current_user_like'] = like
            else:
                joke['current_user_like'] = False
            ret.append(joke)
        return ret

    @classmethod
    def getLatestJokes(cls, user, steps=10):
        jokes = Joke.getLatestJokesList(steps)
        ret = []
        for joke in jokes:
            if user.is_authenticated():
                like = Joke.getLikeStatus(joke['id'],user.id)
                joke['current_user_like'] = like
            else:
                joke['current_user_like'] = False
            ret.append(joke)
        return ret

    @classmethod
    def getRandomJoke(cls):
        seed = 0.00002
        joke = Joke.getRandomJoke(seed)
        while not joke:
            joke = Joke.getRandomJoke(seed)
        return joke

    @classmethod
    def getJoke(cls,jokeid,user):
        joke = Joke.getJoke(jokeid)
        if user.is_authenticated():
            like = Joke.getLikeStatus(jokeid,user.id)
            joke['current_user_like'] = like
        else:
            joke['current_user_like'] = False
        return joke

    @classmethod
    def likeJoke(cls,jokeid,userid):
        jokeid = int(jokeid)
        userid = int(userid)

        return Joke.likeJoke(jokeid,userid)
