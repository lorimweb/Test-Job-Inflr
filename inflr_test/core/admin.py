from django.contrib import admin

from .models import Config, SocialNetwork


class SocialNetworkAdmin(admin.StackedInline):
    model = SocialNetwork


@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    list_display = ('name', 'slogan')
    inlines = [SocialNetworkAdmin]

