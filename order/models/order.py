from django.db import models
from django.contrib.auth.models import User
from product.models import Product  # Importando o modelo Product


class Order(models.Model):
    product = models.ManyToManyField(Product, blank=False) # type: ignore
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    