class SimpleMiddleWare:
    def __init__(self,get_response):
        self.get_response =get_response

    def __call__(self,request):
        response=self.get_responses(request)
        return response    