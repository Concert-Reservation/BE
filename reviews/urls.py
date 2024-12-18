from django.urls import path
from rest_framework.routers import SimpleRouter

from reviews.views import ReviewViewSet

router = SimpleRouter()
router.register('', ReviewViewSet, basename='reviews')

urlpatterns = router.urls
'''
urlpatterns = [
    path('<int:pk>/', ReviewDetail.as_view()),
    path('', ReviewList.as_view()),
]
'''