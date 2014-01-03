#!/usr/bin/env python

"""Some documentation would be nice!"""

from __future__ import print_function
from __future__ import absolute_import

__author__ = 'eric.hanchrow@gmail.com'

from beakerfiddling import cache_manager

@cache_manager.cache('something')
def addone(x):
    print("Laboriously computing result for arg {}".format(x))
    return x + 1
