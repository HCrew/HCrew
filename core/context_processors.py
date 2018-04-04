def logged_in(request):
    return {'logged_in': request.session.get('logged-in', False)}
