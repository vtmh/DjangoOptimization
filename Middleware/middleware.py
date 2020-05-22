# middle ware!
from django.shortcuts import render, redirect

class SessionMiddleWare:

    # Called only once when the serer starts
    def __init__(self, get_response):
        self.get_response = get_response
        print('Session MiddleWare has began')


    # Called for everry new request
    def __call__(self, request):
        response = self.get_response(request)
        print('Session Middleware has been called')
        if 'name' in request.session:
            print(request.session['name'])
        else:
           if not request.path == '/login/':
                return redirect('login')
        return response