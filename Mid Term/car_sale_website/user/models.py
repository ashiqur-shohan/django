from django.db import models
from django.contrib.auth.models import User
from car_model.models import CarModel
# Create your models here.

class History(models.Model):
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    