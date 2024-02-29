from django.shortcuts import render
from . import forms
# Create your views here.

def modelform(request):
    if request.method == "POST":
        form = forms.testForm(request.POST)
        if form.is_valid():
            form.save()  
    else:
        form = forms.testForm()
    return render(request, 'modelform.html', {'form': form})