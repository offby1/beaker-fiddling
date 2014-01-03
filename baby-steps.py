#!/usr/bin/env python

"""
See if I can figure out how to use Beaker
"""

from __future__ import print_function
from __future__ import absolute_import

__author__ = 'ehanchrow@ine.com'

import  ConfigParser
from    beaker.cache          import CacheManager
from    beaker.util           import parse_cache_config_options
from    beakerfiddling.addone import addone
import  os

here = os.path.dirname(os.path.abspath(__file__))
c = ConfigParser.ConfigParser(defaults={'here': here})
c.read(os.path.join(here, 'development.ini'))
cache_manager = CacheManager(**parse_cache_config_options(dict(c.items('app:main'))))

print(addone(0))
print(addone(0))

print(addone(9))
print(addone(9))

cache_manager.region_invalidate(addone, 'region1', 0)
print(addone(0))
print(addone(0))

print(addone(9))
print(addone(9))

# Now interrogate the cache -- see if it has values for 0 and 9 (it
# should, of course).

# TODO -- the leading underscore strongly suggests that I shouldn't be
# accessing _arg_namespace.
c = cache_manager.get_cache(addone._arg_namespace)

for n in range(10):
    print("{}: {}".format(n, "Present" if str(n) in c else "absent"))
