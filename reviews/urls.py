from django.urls import path

from reviews.views import ReviewList, ReviewDetail

urlpatterns = [
    path('<int:pk>/', ReviewDetail.as_view()),
    path('', ReviewList.as_view()),
]