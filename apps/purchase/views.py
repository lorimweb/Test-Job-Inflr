from django.core.urlresolvers import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect

from .models import Purchase
from apps.product.models import Product


class PurchaseView(LoginRequiredMixin, TemplateView):

    template_name = 'admin/admin.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        try:
            obj_purchase = Purchase()
            obj_purchase.user = self.request.user
            obj_purchase.product = context['object']
            obj_purchase.save()
        except:
            return HttpResponseRedirect(reverse('purchases', args=args, kwargs=kwargs))

        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(PurchaseView, self).get_context_data(**kwargs)

        context['object'] = Product.objects.get(slug=kwargs.get('slug'))

        return context