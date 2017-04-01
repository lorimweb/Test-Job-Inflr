from django.conf.urls import url

from .views import ProductListView, ProductDetailView

urlpatterns =[
    url(r'^(?P<slug>[-_\w]+)/$', ProductDetailView.as_view(), name="product_detail"),
    url(r'^$', ProductListView.as_view(), name='product_list'),
]
