from rest_framework.view import ModelView # type: ignore

from product.models import Product
from product.serializers.product_serializer import ProductSerializer


class ProductView(ModelView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all().order_by("id")