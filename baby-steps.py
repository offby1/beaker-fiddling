#!/usr/bin/env python

"""
See if I can figure out how to use Beaker
"""

from __future__ import print_function
from __future__ import absolute_import

__author__ = 'ehanchrow@ine.com'

from beaker.cache import CacheManager
from beaker.util import parse_cache_config_options

cache_manager = CacheManager(**parse_cache_config_options({'cache.type': 'memory'}))

@cache_manager.cache('something')
def addone(x):
    print("Laboriously computing result for arg {}".format(x))
    return x + 1

print(addone(0))
print(addone(0))

print(addone(9))
print(addone(9))

cache_manager.invalidate(addone, 'something', 0)
print(addone(0))
print(addone(0))

print(addone(9))
print(addone(9))
