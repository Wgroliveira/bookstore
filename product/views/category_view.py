from rest_framework.view import ModelView # type: ignore

from product.models import Category
from product.serializers.category_serializer import CategorySerializer


class CategoryView(ModelView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all().order_by("id")