from pyramid.config import Configurator

from beaker.cache import CacheManager
from beaker.util import parse_cache_config_options
cache_manager = CacheManager(**parse_cache_config_options({'cache.type': 'memory'}))

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.scan()
    return config.make_wsgi_app()
