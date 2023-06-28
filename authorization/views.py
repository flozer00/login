from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class Login(View):
    #def authorization_page(request):
    template_name = 'authorization.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        if(request.POST):
            login_data = request.POST.dict()
            username = login_data.get('username')
            email = login_data.get('email')
            password = login_data.get('password')
            print(username, email, password)
            return HttpResponse('This a post request')
        else:
            return render(request, self.template_name)

