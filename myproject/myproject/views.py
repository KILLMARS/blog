# from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse('Hello, World! Im homepage')
    return render(request, 'home.html')

def about(request):
    # return HttpResponse('About me page.')
    return render(request, 'about.html')