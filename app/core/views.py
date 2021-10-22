from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from . import models, serializers, filtersets, pagination


class ActivityViewSet(viewsets.ModelViewSet):
    """A viewset of Activity model"""
    queryset = models.Activity.objects.all()
    serializer_class = serializers.ActivitySerializer
    permission_classes = []

    filter_backends = [
        DjangoFilterBackend
    ]
    filterset_class = filtersets.ActivityFilterSet
    pagination_class = pagination.CustomPagination

    lookup_field = 'slug'


class BoxViewSet(viewsets.ModelViewSet):
    """A ViewSet of Box model"""
    queryset = models.Box.objects.all()
    serializer_class = serializers.BoxSerializer
    permission_classes = []
    lookup_field = 'slug'


class CategoryViewSet(viewsets.ModelViewSet):
    """A ViewSet of Category model"""
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = []
    lookup_field = 'slug'
