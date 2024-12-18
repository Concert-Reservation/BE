from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(null=True, max_length=50)
    content = models.TextField(null=True, max_length=500)
    genre = models.CharField(null=True,max_length=50)
    venue = models.CharField(null=True,max_length=50)
    date_concert = models.IntegerField(null=True, default=0, validators=[MinValueValidator(1960), MaxValueValidator(2025)])
    rating = models.IntegerField(null=True,default=0, validators=[MinValueValidator(0),MaxValueValidator(10)])
    date_reviewed = models.DateTimeField(null=True, auto_now_add=True)

    def __str__(self):
        return self.title

    def clean(self):
        if self.content is not None:
            if len(self.content) > 500:
                raise ValidationError({'content': 'Ensure this value has at most 500 characters.'})
