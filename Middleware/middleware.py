# middle ware!

class SessionMiddleWare:
    # Called only once when the serer starts
    def __init__(self, get_response):
        self.get_response = get_response

    # Called for everry new request
    def __call__(self, request):
        response = self.get_response(request)
        return response