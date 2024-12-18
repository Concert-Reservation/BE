from django.shortcuts import render
from rest_framework import generics

from reviews.models import Review
from reviews.serializers import ReviewSerializer


# Create your views here.

class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer