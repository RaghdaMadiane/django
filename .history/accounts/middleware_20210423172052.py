class SimpleMiddleWare:
    def __init__(self,get_response):
        self.get_response =get_response

    def __call__(self,request):
        if request.user.is_active:
            return self.get_response(request)
        
        return HttpResponseForbidden("you are not an active user")   