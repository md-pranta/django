from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    roll = models.IntegerField(primary_key=True)
    address = models.TextField()
    father_name = models.CharField(default = "ffff", max_length=50)
    
    def __str__(self):
        return f"roll: {self.roll} name: {self.name}"
    