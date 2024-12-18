from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(null=True, max_length=50)
    content = models.TextField(null=True, max_length=500)
    genre = models.CharField(null=True,max_length=50)
    venue = models.CharField(null=True,max_length=50)
    date_concert = models.DateTimeField(null=True)
    rating = models.IntegerField(null=True,default=0)
    date_reviewed = models.DateTimeField(null=True, auto_now_add=True)

    def __str__(self):
        return self.title