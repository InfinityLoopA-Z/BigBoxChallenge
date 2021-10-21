from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


from . import models, serializers


class StandardResultsSetPagination(PageNumberPagination):

    """A results Pagination"""

    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

    def get_paginated_response(self, data):
        return Response({
            'links': {
               'next': self.get_next_link(),
               'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'results': data
        })


class BoxViewSet(viewsets.ModelViewSet):
    """A ViewSet of the Box model"""
    queryset = models.Box.objects.all()
    serializer_class = serializers.BoxSerializerFather
    permission_classes = []
    lookup_field = 'slug'


class CategoryViewSet(viewsets.ModelViewSet):
    """A ViewSet of the Category model"""
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = []
