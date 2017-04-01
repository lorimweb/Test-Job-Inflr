from django.contrib import admin
from .models import Product


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ('name', 'user', 'price')

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()
