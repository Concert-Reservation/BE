from rest_framework import serializers

from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'author', 'title', 'content', 'genre', 'venue', 'date_concert', 'rating', 'date_reviewed')
        model = Review
