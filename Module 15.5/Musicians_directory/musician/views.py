from django.shortcuts import render
from .models import musician_directory
from album.models import AlbumModel
# Create your views here.

def home(request):
    music = musician_directory.objects.all()
    album = AlbumModel.objects.all()
    return render(request,'home.html',{'album':album})