# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import random
# Create your views here.
#function based views
'''
def home(request):
    html_ = """<!DOCTYPE html>
    <html lang=en>
    <head>
    </head>
    <body>
    <h1>Hello World!</h1>
    <p>This is html coming through</p>
    </body>
    </html>
    """
    
    #return HttpResponse("Hello")
    #return render(request, "home.html", {})
    return HttpResponse(html_)
'''
def home(request):
    num = None
    condition_bool_item = True
    some_list = [
            random.randint(0,100000),
                 random.randint(0,100000),
                 random.randint(0,100000)
                 ]

    if condition_bool_item:
        num = random.randint(0,100000)
    context = {
               "num": num,
               "some_list": some_list
               }
    return render(request, "home.html", context)

def about(request):

    context = {

               }
    return render(request, "about.html", context)

def contact(request):

    context = {

               }
    return render(request, "contact.html", context)

