from apps.product.models import Product
from inflr_test.core.models import Config


def home(request):
    products = Product.objects.order_by('-id')[0:6]
    config = Config.objects.last()

    return {
        'products': products,
        'config': config,
    }