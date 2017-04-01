from django.conf.urls import url

from .views import PurchaseView

urlpatterns = [
    url(r'^(?P<slug>[-_\w]+)/$', PurchaseView.as_view(), name='purchases'),
]
