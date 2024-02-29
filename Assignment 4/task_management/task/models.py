from django.db import models
from category.models import Category
from django import forms
# Create your models here.


class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=100)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)
    Task_assign_date = models.DateField(default='2023-01-01')
    category = models.ManyToManyField(Category)

    def __str__(self) -> str:
        return f"{self.taskTitle}"