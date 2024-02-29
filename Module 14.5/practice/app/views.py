from django.shortcuts import render
from . forms import TestForm
# Create your views here.

def home(request):
    if request.method == "POST":
        form = TestForm(request.Post)
        if form.is_valid():
            print(form)
    else:
        form = TestForm()
    return render(request,'home.html',{'form':form})