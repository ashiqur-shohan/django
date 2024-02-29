from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.show_tasks,name='show_task'),
    path('add_task/', views.add_task,name='add_task'),
    path('edit_task/<int:id>', views.edit_task,name='edit_task'),
]