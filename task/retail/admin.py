from django.contrib import admin

from task.product.admin import ProductInline
from task.retail.models import RetailNetwork


class RetailNetworkAdmin(admin.ModelAdmin):
    """Класс для управления отображением административной панели записей о розничных сетях."""
    list_display = ('name', 'email', 'country', 'city', 'factory')
    search_fields = ('name', 'email', 'country', 'city', 'factory__name')
    list_filter = ('country', 'city')
    inlines = [ProductInline]

    def get_formsets_with_inlines(self, request, obj=None):
        for inline in self.get_inline_instances(request, obj):
            if isinstance(inline, ProductInline):
                kwargs = {
                    'fk_name': 'retail_network',
                    'can_delete': False,
                }
                yield inline.get_formset(request, obj, **kwargs), inline

            else:
                yield inline.get_formset(request, obj), inline

admin.site.register(RetailNetwork, RetailNetworkAdmin)
