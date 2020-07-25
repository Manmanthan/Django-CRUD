from rest_framework import viewsets, generics, filters

from .serializers import CustomerSerializer, ProductSerializer, OrderSerializer
from .models import Customers, Products, Orders


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customers.objects.all().order_by('customerid')
    serializer_class = CustomerSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all().order_by('supplierid')
    serializer_class = ProductSerializer


class OrdersViewSet(generics.ListCreateAPIView):
    search_fields = ['customerid__customerid']
    filter_backends = (filters.SearchFilter,)
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer