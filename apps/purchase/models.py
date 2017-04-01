from django.db import models
from apps.accounts.models import User
from apps.product.models import Product


class Purchase(models.Model):
    user = models.ForeignKey(User, null=True, editable=False)
    product = models.ForeignKey(Product, null=True, editable=False)
    date_purchase = models.DateTimeField('Data da Compra', auto_now_add=True)

    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'
