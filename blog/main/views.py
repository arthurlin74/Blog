<<<<<<< HEAD
﻿from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse


def main(request):
    '''
    Show 'Hello world!' in the main page
    '''
    context = {'like':'Django 很棒'}
    return render(request, 'main/main.html', context)

def about(request):
    '''
    Render the about page
    '''
    return render(request, 'main/about.html')
=======
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def main(request):
    '''
    Show 'Hello world!' in the main page
    '''
    return HttpResponse('Hello world!')
>>>>>>> branch 'master' of https://github.com/arthurlin74/blog
