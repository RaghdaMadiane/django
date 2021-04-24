from django.http import HttpResponseForbidden
class SimpleMiddleWare:
    def __init__(self,get_response):
        self.get_response =get_response

    def __call__(self,request):
        if request.user.username:
            if request.user.is_active:
                return self.get_response(request)
        
            return HttpResponseForbidden("you are not an active user,you can contact the admin ")  
        else:
            return self.get_response(request)
    # def __call__(self,request):
       
    #     if request.user.is_active:
    #         return self.get_response(request)
        
    #     return HttpResponseForbidden("you are not an active user,you can contact the admin ")  
        