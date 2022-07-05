from django.db import models


# Create your models here.
class Team(models.Model):
    First_Name = models.CharField(max_length=255)
    Last_Name = models.CharField(max_length=255)
    Designations = models.CharField(max_length=255)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    Facebook = models.URLField(max_length=100)
    Google = models.URLField(max_length=100)
    Twitter = models.URLField(max_length=100)
    Date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.First_Name
