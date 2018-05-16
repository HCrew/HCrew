def logged_in(request):
    return {'logged_in': 'user' in request.session}


def user_type(request):
    return {'user_type': request.session.get('user_type')}
