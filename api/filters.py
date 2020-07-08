from django_filters import FilterSet,filters

from api.models import Computer

class LimitFilter:
    def filter_queryset(self,request,queryset,view):
        limit=request.query_params['limit']
        print(limit)
        if limit:
            limit=int(limit)
            return queryset[:limit]
        return queryset

class ComputerFilterSet(FilterSet):
    class Meta:
        model = Computer
        fields = ['name','price','brand']
    max_price=filters.NumberFilter(field_name='price',lookup_expr='lte')
    min_price=filters.NumberFilter(field_name='price',lookup_expr='gte')


