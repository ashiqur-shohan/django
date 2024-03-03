from django import forms
from .models import musician_directory
class AlbumForm(forms.ModelForm):
    class Meta:
        model = musician_directory
        fields = '__all__'