from django.views.generic import CreateView, UpdateView, FormView, ListView, DeleteView
from .forms import UserAdminCreationForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm
from apps.product.models import Product
from apps.purchase.models import Purchase

from .models import User


class MyProductsView(LoginRequiredMixin, ListView):
    template_name = 'admin/myproducts.html'

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user).all()


class AdminView(LoginRequiredMixin, ListView):
    template_name = 'admin/admin.html'

    def get_queryset(self):
        return Purchase.objects.filter(user=self.request.user).all()


class RegisterView(CreateView):
    model = User
    template_name = 'admin/register.html'
    form_class = UserAdminCreationForm
    success_url = reverse_lazy('login')


class UpdateUserView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'admin/update_user.html'
    fields = ['name', 'email']
    success_url = reverse_lazy('accounts:admin')

    def get_object(self):
        return self.request.user


class UpdatePasswordView(LoginRequiredMixin, FormView):
    template_name = 'admin/update_password.html'
    form_class = PasswordChangeForm
    success_url = reverse_lazy('accounts:admin')

    def get_form_kwargs(self):
        kwargs = super(UpdatePasswordView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class InsertProductView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'admin/insert_product.html'
    fields = "__all__"
    success_url = reverse_lazy('accounts:myproducts')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(InsertProductView, self).form_valid(form)


class UpdateProductView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = 'admin/update_product.html'
    fields = "__all__"
    success_url = reverse_lazy('accounts:myproducts')


class DeleteProductView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'admin/product_confirm_delete.html'
    success_url = reverse_lazy('accounts:myproducts')