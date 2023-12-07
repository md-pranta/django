from django.db import models
from musicians.models import Musician
# Create your models here.


class Album(models.Model):
    album_name = models.CharField(max_length=30)
    release = models.DateField()
    
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    
    choice = [('1', '1'),('2', '2'),('3', '3'),('4', '4'),('5', '5'),]
    
    rating = models.CharField(max_length=5,default='0',choices = choice)
    
    def __str__(self) -> str:
        return self.album_name