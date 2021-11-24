from django import urls
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()

router.register("categories", views.CategoryViewSet)
router.register("boxes", views.BoxViewSet)
router.register("activities", views.ActivityViewSet)

urlpatterns = [
    urls.path("", urls.include((router.urls, "routers"), namespace="routers")),
]
