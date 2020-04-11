from rest_framework.pagination import PageNumberPagination
from . import PaginationHandlerMixin


class BasicPagination(PageNumberPagination):
    page_size_query_param = 'limit'
