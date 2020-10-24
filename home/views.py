from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import Account


def home(request):
    return render(request, 'login.html')

class submit(TemplateView):
    template_name = 'thankyou.html'

    def post(self, request):
        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        Account(username=username, password=password).save()
        return render(request, self.template_name)
    