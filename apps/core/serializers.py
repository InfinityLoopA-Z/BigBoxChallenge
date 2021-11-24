from rest_framework import serializers

from . import models


class BoxImageSerializer(serializers.ModelSerializer):
    """A BoxImage Serializer (Child of Box)"""
    class Meta:
        model = models.BoxImage
        exclude = []


class BoxSerializer(serializers.ModelSerializer):
    """A Box Serializer (Father of BoxImage"""
    boximage_set = BoxImageSerializer(many=True, allow_null=True)

    class Meta:
        model = models.Box
        fields = [
            'name',
            'slug',
            'price',
            'internal_name',
            'description',
            'category',
            'purchase_available',
            'boximage_set',
        ]
        lookup_field = 'slug'
        extra_kwargs = {'url': {'lookup_field': 'slug'}}


class CategorySerializer(serializers.ModelSerializer):
    """A Categories serializer"""

    box_set = BoxSerializer(many=True, allow_null=True)

    class Meta:
        model = models.Category
        fields = [
            'order',
            'name',
            'slug',
            'description',
            'box_set'
        ]
        lookup_field = 'slug'
        extra_kwargs = {'url': {'lookup_field': 'slug'}}


class ReasonSerializer(serializers.ModelSerializer):
    """A Reason Serializer"""
    class Meta:
        model = models.Reason
        exclude = []


class ActivityImageSerializer(serializers.ModelSerializer):
    """A ActivityImage Serializer (Child of Activity)"""
    class Meta:
        model = models.ActivityImage
        exclude = []


class ActivitySerializer(serializers.ModelSerializer):
    """A Activity Serializer"""
    box_set = BoxSerializer(many=True, allow_null=True)
    reasons = ReasonSerializer(many=True, allow_null=True)
    activityimage_set = ActivityImageSerializer(many=True, allow_null=True)

    class Meta:
        model = models.Activity
        fields = [
            'name',
            'slug',
            'internal_name',
            'category',
            'description',
            'purchase_available',
            'reasons',
            'activityimage_set',
            'box_set'
        ]
        lookup_field = 'slug'
        extra_kwargs = {'url': {'lookup_field': 'slug'}}
