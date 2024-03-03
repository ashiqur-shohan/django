from django.urls import path, include
from . import views
urlpatterns = [
    path('details/<int:id>', views.DetailCarView.as_view(), name='car_detail'),
    path('buy_car/<int:id>', views.buy_car, name='buy_car'),
]