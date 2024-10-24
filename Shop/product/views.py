from itertools import product

from rest_framework.generics import ListAPIView

from .models import Product
from .serializer import ProductSerializer

class ListProductView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

