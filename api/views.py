from django.shortcuts import render
from rest_framework.generics import ListAPIView
from api.serializers import ComputerModelSerializer
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from api.pagenations import MyPageNumberPagination,MyLimitoffsetPagination
from api.filters import ComputerFilterSet,LimitFilter
# Create your views here.
from api.models import Computer


class ComputerListAPIView(ListAPIView):
    queryset = Computer.objects.all()
    serializer_class = ComputerModelSerializer
    filter_backends = [SearchFilter,OrderingFilter,LimitFilter,DjangoFilterBackend]
    search_fields = ['name','price']
    ordering = ['price']
    # pagination_class = MyPageNumberPagination
    # pagination_class = MyLimitoffsetPagination
    filter_class = ComputerFilterSet



