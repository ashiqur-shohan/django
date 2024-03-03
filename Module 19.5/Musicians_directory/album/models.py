from django.db import models
from musician.models import musician_directory
# Create your models here.

class AlbumModel(models.Model):
    album_name = models.CharField(max_length = 30)
    album_release_date = models.DateField()
    CHOICES = [('1', 'One'), ('2', 'Two'), ('3', 'Three'), ('4', 'Four'), ('5', 'Five')]
    rating = models.CharField(choices = CHOICES,max_length = 30)
    musician = models.ForeignKey(musician_directory,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.album_name