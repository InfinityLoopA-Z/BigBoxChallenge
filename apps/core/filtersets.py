from django_filters.rest_framework import filters
from django_filters.rest_framework.filterset import FilterSet

from . import models


class ActivityFilterSet(FilterSet):
    category_id = filters.NumberFilter(field_name='category__id')
    reason_id = filters.NumberFilter(field_name='reasons__id')
    box_slug = filters.CharFilter(field_name="box__slug")

    class Meta:
        model = models.Activity
        fields = [
        ]
