from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from reviews.models import Review
from reviews.permissions import IsAuthorOrReadOnly
from reviews.serializers import ReviewSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthorOrReadOnly, IsAuthenticated]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewByAuthorViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(author=self.request.user)