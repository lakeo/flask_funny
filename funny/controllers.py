# -*- coding: utf-8 -*-
from models import Joke
import random

class JokeController(object):

    @classmethod
    def getJokes(cls,index=10000000,step=10):
        jokes = Joke.getJokesList(index,step)
        ret = []
        for joke in jokes:
            ret.append(joke)
        return ret

    @classmethod
    def getLatestJokes(cls, steps=10):
        jokes = Joke.getLatestJokesList(steps)
        ret = []
        for joke in jokes:
            ret.append(joke)
        return ret

    @classmethod
    def getRandomJoke(cls):
        seed = 0.00002
        joke = Joke.getRandomJoke(seed)
        while not joke:
            joke = Joke.getRandomJoke(seed)
        return joke

