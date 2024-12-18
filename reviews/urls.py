from rest_framework.routers import SimpleRouter

from reviews.views import ReviewViewSet, ReviewByAuthorViewSet

router = SimpleRouter()
router.register('by-author', ReviewByAuthorViewSet, basename='reviews-by-author')
router.register('', ReviewViewSet, basename='reviews')
urlpatterns = router.urls
