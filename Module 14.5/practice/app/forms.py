from django import forms
from django.forms.widgets import NumberInput

class TestForm(forms.Form):
    name = forms.CharField()
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
    email = forms.EmailField()
    agree = forms.BooleanField()
    data = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))