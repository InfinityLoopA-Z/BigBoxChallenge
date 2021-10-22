from rest_framework import pagination
from rest_framework.response import Response


class CustomPagination(pagination.LimitOffsetPagination):
    """ Custom pagination limit offset. """

    default_limit = 2
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    max_limit = 20

    def get_paginated_response(self, data):
        response = Response(data)
        return response
