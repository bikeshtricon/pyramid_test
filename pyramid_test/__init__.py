from pyramid.config import Configurator

#Added a comment by Vijay mearged
def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application...
    """
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    
    config.add_route('home', '/')
    
    config.add_route('page2', '/page2')
    
    
    #config.add_route('page3', '/page3')
    #config.add_route('page4', '/page4') #By vk bbbbbbbbb
    
    
    config.scan()
    return config.make_wsgi_app()
