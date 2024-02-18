from django.shortcuts import render
import datetime
# Create your views here.

def home(request):
    data = {'lst':['ashiqur','rahman','shohan'],
            'test':'python',
            'birthday':datetime.datetime.now,
            'num':10,
            'string':'I love python',
            }
    return render(request,'home.html',data)
