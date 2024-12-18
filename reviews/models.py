from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

class Review(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=500)
    genre = models.CharField(max_length=50)
    venue = models.CharField(max_length=50)
    date_concert = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    date_reviewed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title