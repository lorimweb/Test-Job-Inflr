from django.conf.urls import url

from .views import RegisterView, AdminView, MyProductsView, UpdateUserView, UpdatePasswordView, InsertProductView, UpdateProductView, DeleteProductView

urlpatterns = [
    url(r'^registro/', RegisterView.as_view(), name='register'),
    url(r'^$', AdminView.as_view(), name='admin'),
    url(r'^meus-produtos/$', MyProductsView.as_view(), name='myproducts'),
    url(r'^alterar-dados/$', UpdateUserView.as_view(), name='update_user'),
    url(r'^alterar-senha/$', UpdatePasswordView.as_view(), name='update_password'),
    url(r'^novo-produto/$', InsertProductView.as_view(), name='insert_product'),
    url(r'^editar-produto/(?P<slug>[-_\w]+)/$', UpdateProductView.as_view(), name='update_product'),
    url(r'^delete-produto/(?P<slug>[-_\w]+)/$', DeleteProductView.as_view(), name='delete_product'),
]
