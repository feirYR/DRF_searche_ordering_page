from rest_framework.pagination import PageNumberPagination
from rest_framework.pagination import LimitOffsetPagination
class MyPageNumberPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page'
    max_page_size = 5
    page_size_query_param = 'page_size'

class MyLimitoffsetPagination(LimitOffsetPagination):
    default_limit = 4
    limit_query_param = 'limit'
    offset_query_param = 'offset'

