from rest_framework import filters
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from task.entrepreneur.models import IndividualEntrepreneur
from task.entrepreneur.serializers import IndividualEntrepreneurSerializer
from task.network.views import IsStaffOrReadOnly


class IndividualEntrepreneurListCreateView(ListCreateAPIView):
    serializer_class = IndividualEntrepreneurSerializer
    permission_classes = [IsStaffOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name', 'country']

    def get_queryset(self):
        queryset = IndividualEntrepreneur.objects.all()
        country = self.request.query_params.get('country', None)
        if country is not None:
            queryset = queryset.filter(country=country)
        return queryset


class IndividualEntrepreneurView(RetrieveUpdateDestroyAPIView):
    queryset = IndividualEntrepreneur.objects.all()
    serializer_class = IndividualEntrepreneurSerializer
    permission_classes = [IsStaffOrReadOnly]

    def update(self, request, *args, **kwargs):
        # forbid update of 'debt' field
        request.data.pop('debt', None)
        return super().update(request, *args, **kwargs)
