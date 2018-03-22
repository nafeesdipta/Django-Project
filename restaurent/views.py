from django.template import Template, Context
from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views he

def index(request):
    now = datetime.datetime.now()
    
    context = {
        'current_date': now
        }
    return render(request, "../templates/t.html", context)