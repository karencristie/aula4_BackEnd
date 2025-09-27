from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class CleintAdmn(admin.ModelAdmin):
    list_display = ('nome', 'email', 'idade', 'ativo')
    search_fields = ('nome', 'email')
