from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    return render(request, 'userInfo/index.html')
    # template = loader.get_template('index.html')
    # return HttpResponse(template.render())

def login(request):
    return render(
        request,
        'userInfo/login.html'
    )

def join(request):
    return render(
        request,
        'userInfo/join.html'
    )
