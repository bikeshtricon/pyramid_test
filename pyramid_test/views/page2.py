from pyramid.view import view_config


@view_config(route_name='page2', renderer='../templates/mytemplate.pt')
def my_view(request):
    return {'project': 'pyramid_test page2'}
