#!/usr/bin/env python

"""Some documentation would be nice!"""

from __future__ import print_function
from __future__ import absolute_import

__author__ = 'eric.hanchrow@gmail.com'

from beaker import cache


def _addone(x):
    print("Laboriously computing result for arg {}".format(x))
    return x + 1

addone = cache.cache_region('region1')(_addone)
