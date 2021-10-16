from drf_writable_nested.serializers import WritableNestedModelSerializer
from rest_framework import serializers

from . import models


class BoxImageSerializer(serializers.ModelSerializer):
    """A serializer for Boximages"""
    class Meta:
        model = models.BoxImage
        exclude = []


class BoxSerializer(WritableNestedModelSerializer):
    """A serializer for Boxes"""
    box_image = BoxImageSerializer(many=True, allow_null=True)

    class Meta:
        model = models.Box
        exclude = []


class ActivityImageSerializer(serializers.ModelSerializer):
    """A serializer for ActivityImage"""
    class Meta:
        model = models.ActivityImage
        exclude = []


class ActivitySerializer(WritableNestedModelSerializer):
    """A serializer for """
    box_image = ActivityImageSerializer(many=True, allow_null=True)

    class Meta:
        model = models.Activity
        exclude = []


class CategorySerializer(serializers.ModelSerializer):
    """A serializer for Categories"""
    class Meta:
        model = models.Category
        exclude = []


class ReasonSerializer(serializers.ModelSerializer):
    """A serializer for Reasons"""
    class Meta:
        model = models.Reason
        exclude = []
