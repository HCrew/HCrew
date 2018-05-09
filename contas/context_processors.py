def logged_in(request):
    return {'logged_in': 'user' in request.session}
