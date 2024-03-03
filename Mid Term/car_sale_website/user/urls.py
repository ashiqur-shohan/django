from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('profile/edit', views.edit_profile, name='edit_profile'),
    path('/profile/edit/pass_change/', views.pass_change, name='pass_change'),
    path('logout/', views.user_logout, name='user_logout'),
]