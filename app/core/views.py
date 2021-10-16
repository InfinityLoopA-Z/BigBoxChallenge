from rest_framework import viewsets

from . import models, serializers


class BoxViewSet(viewsets.ModelViewSet):
    """A ViewSet  of the box model (Father of BoxImage)"""
    queryset = models.Box.objects.all()
    serializer_class = serializers.BoxSerializer
    permission_classes = []


class BoxImageViewSet(viewsets.ModelViewSet):
    """A viewSet of the BoxImage Model (Child of Box)"""
    queryset = models.BoxImage.all()
    serializer_class = serializers.BoxImageSerializer
    permission_classes = []


class ActivityViewSet(viewsets.ModelViewSet):
    """A ViewSet of the Activity model"""
    queryset = models.Activity.objects.all()
    serializer_class = serializers.ActivitySerializer
    permission_classes = []


class ActivityImageViewSet(viewsets.ModelViewSet):
    """A ViewSet of the ActivityImage model"""
    queryset = models.ActivityImage.objects.all()
    serializer_class = serializers.ActivityImageSerializer
    permission_classes = []


class CategoryViewSet(viewsets.ModelViewSet):
    """A ViewSet of the Category model"""
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = []


class ReasonViewSet(viewsets.ModelViewSet):
    """A ViewSet of the Reason model"""
    queryset = models.Reason.objects.all()
    serializer_class = serializers.ReasonSerializer
    permission_classes = []
