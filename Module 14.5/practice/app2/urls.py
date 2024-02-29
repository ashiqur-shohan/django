from django.urls import path,include
from . views import modelform
urlpatterns = [
    path('', modelform),
]