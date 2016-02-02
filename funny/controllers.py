# -*- coding: utf-8 -*-
from models import Joke

class JokeController(object):
    @classmethod
    def getRandomJoke(cls):
        return Joke.getRandomJoke()

    @classmethod
    def getJokes(cls,index=10000000,step=20):
        jokes = Joke.getJokesList(index,step)
        ret = []
        for joke in jokes:
            ret.append(joke)
        return ret

    @classmethod
    def getLatestJokes(cls, steps=20):
        jokes = Joke.getLatestJokesList(steps)
        ret = []
        for joke in jokes:
            ret.append(joke)
        return ret
