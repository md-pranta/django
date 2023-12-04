from django.db import models

# Create your models here.
class PracticeModel(models.Model):
    name = models.CharField(max_length=155)
    auto = models.AutoField(primary_key=True)
    # big_auto = models.BigAutoField()
    big_int = models.BigIntegerField()
    
    binary = models.BinaryField()
    bol = models.BooleanField()
    date = models.DateField()
    dateTime = models.DateTimeField()
    
    duration = models.DurationField()
    # file = models.FileField(upload_to='path/')
    # foreign = models.ForeignKey('othermodel', on_delete=models.CASCADE)
    ip = models.GenericIPAddressField()
    # img = models.ImageField(upload_to='path/')
    json = models.JSONField()
    
    
    # manyTomany = models.ManyToManyField('othermodel')
    # oneToone = models.OneToOneField('otherModel', on_delete=models.CASCADE)
    slug = models.SlugField()
    
    time = models.TimeField()
    url = models.URLField()
     
    
    
    def __str__(self) -> str:
        return f"name: {self.name} auto: {self.auto}"
    