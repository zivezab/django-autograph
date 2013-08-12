from django.contrib import admin

from autograph.models import Autograph


class AutographAdmin(admin.ModelAdmin):
    list_display = ('user', 'timestamp',)
    search_fields = ['user', ]

admin.site.register(Autograph, AutographAdmin)