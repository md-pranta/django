from django.db import models
from catagories.models import Catagory
from authors.models import Author
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    # many to many relationship with catagories
    catagory = models.ManyToManyField(Catagory)
    # many to one relationship with authors
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.title