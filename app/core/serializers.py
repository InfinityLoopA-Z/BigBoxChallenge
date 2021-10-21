from rest_framework import serializers

from . import models


class BoxImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BoxImage
        exclude = []


class BoxSerializerFather(serializers.ModelSerializer):
    """A serializer for box"""
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


class BoxSerializer(serializers.ModelSerializer):
    """ A serializer for box """

    class Meta:
        model = models.Box
        fields = [
            'name',
            'slug',
            'price',
        ]


class CategorySerializer(serializers.ModelSerializer):
    """A serializer for Categories"""

    box_set = BoxSerializer(many=True, allow_null=True)

    class Meta:
        model = models.Category
        fields = [
            'name',
            'slug',
            'description',
            'box_set'
        ]
