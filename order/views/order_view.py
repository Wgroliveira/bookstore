from rest_framework.view import ModelView

from order.models import Order
from order.serializers import OrderSerializer


class OrderView(ModelView):

    serializer_class = OrderSerializer
    queryset = Order.objects.all().order_by("id")