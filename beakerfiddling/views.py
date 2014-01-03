from pyramid.view import view_config

from beakerfiddling.addone import addone

@view_config(route_name='home', renderer='json')
def my_view(request):
    print("Serving 'em up, boss")
    return {'hello': 'world',
            'one more than 17 is': addone(17)}
