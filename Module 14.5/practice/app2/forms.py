from django import forms
from app2.models import testModel

class testForm(forms.ModelForm):
    class Meta:
        model=testModel
        fields = "__all__"
        