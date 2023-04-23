from rest_framework import filters
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from task.factory.models import Factory
from task.factory.serializers import FactorySerializer
from task.network.views import IsStaffOrReadOnly


# Create your views here.
class FactoryListCreateView(ListCreateAPIView):
    serializer_class = FactorySerializer
    permission_classes = [IsStaffOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name', 'country']

    def get_queryset(self):
        queryset = Factory.objects.all()
        country = self.request.query_params.get('country', None)
        if country is not None:
            queryset = queryset.filter(country=country)
        return queryset


class FactoryView(RetrieveUpdateDestroyAPIView):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer
    permission_classes = [IsStaffOrReadOnly]

    def update(self, request, *args, **kwargs):
        # forbid update of 'debt' field
        request.data.pop('debt', None)
        return super().update(request, *args, **kwargs)
