from django.db import models

# Create your models here.

class testModel(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    father_name = models.CharField(max_length=30)
    address = models.TextField()

    def __str__(self) -> str:
        return f"{self.name}"