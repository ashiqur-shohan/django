from django.db import models
# from django.contrib.auth.models import User
from brand.models import BrandModel

# Create your models here.


class CarModel(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    car_price = models.IntegerField()
    car_qty = models.IntegerField()
    brand = models.ForeignKey(BrandModel, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='uploads/', blank=True, null=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    car_model = models.ForeignKey(
        CarModel, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comments by {self.name}'
