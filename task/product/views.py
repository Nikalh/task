from rest_framework import filters
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from task.network.views import IsStaffOrReadOnly
from task.product.models import Product
from task.product.serializers import ProductSerializer


class ProductListCreateView(ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsStaffOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name', 'country']

    def get_queryset(self):
        queryset = Product.objects.all()
        country = self.request.query_params.get('country', None)
        if country is not None:
            queryset = queryset.filter(country=country)
        return queryset


class ProductView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsStaffOrReadOnly]

    def update(self, request, *args, **kwargs):
        # forbid update of 'debt' field
        request.data.pop('debt', None)
        return super().update(request, *args, **kwargs)
