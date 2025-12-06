from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, ArticleViewSet

router = DefaultRouter()
router.register("articles", ArticleViewSet)
router.register("categories", CategoryViewSet)

urlpatterns = router.urls
