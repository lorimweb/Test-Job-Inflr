from django.db import models
from decimal import Decimal
from django_extensions.db.fields import AutoSlugField
from apps.accounts.models import User


class Product(models.Model):
    user = models.ForeignKey(User, related_name='User', null=True, editable=False)
    name = models.CharField('Nome', max_length=100)
    slug = AutoSlugField('slug', max_length=255, unique=True, populate_from=('name',))
    price = models.DecimalField('Preço', max_digits=8, decimal_places=2, default=Decimal('0.00'))
    img = models.ImageField('Imagem', blank=True)
    img_url = models.CharField('Imagem Url', blank=True, max_length=255)
    description = models.TextField('Conteudo')

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        args = [
            self.slug
        ]
        return ('product_detail', args)
