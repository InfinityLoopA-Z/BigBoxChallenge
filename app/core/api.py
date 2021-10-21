from django import urls
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()

router.register("category", views.CategoryViewSet)
router.register("boxes", views.BoxViewSet)

urlpatterns = [
    urls.path("", urls.include((router.urls, "routers"), namespace="routers")),
]
