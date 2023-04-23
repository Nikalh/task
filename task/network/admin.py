from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.db.models import F
from .models import (Supplier, NetworkNode, )
from ..product.admin import ProductInline


class NetworkNodeAdmin(admin.ModelAdmin):
    """Класс, настраивающий административную панель для модели NetworkNode."""

    list_display = ('name', 'email', 'country', 'city', 'street', 'house_number')
    list_filter = ('country', 'city')
    actions = ['clear_debt']

    def clear_debt(self, request, queryset):
        """Метод для обнуления задолженности перед поставщиком у выбранных записей."""

        queryset.update(debt=0)

    # Отображаемое имя для действия обнуления задолженности.
    clear_debt.short_description = _("Очистить задолженность перед поставщиком")

    def get_queryset(self, request):
        """Метод для получения списка записей с дополнительным полем supplier_name, содержащим имя поставщика."""

        qs = super().get_queryset(request)
        qs = qs.annotate(supplier_name=F('supplier__name'))
        return qs

    def supplier_name(self, obj):
        return obj.supplier_name

    supplier_name.short_description = "Поставщик"
    inlines = [ProductInline]


admin.site.register(Supplier)
admin.site.register(NetworkNode, NetworkNodeAdmin)
