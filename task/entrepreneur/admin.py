from django.contrib import admin

from task.entrepreneur.models import IndividualEntrepreneur
from task.product.admin import ProductInline


class IndividualEntrepreneurAdmin(admin.ModelAdmin):
    """Класс для управления отображением административной панели записей об индивидуальных предпринимателях."""

    list_display = ('name', 'email', 'country', 'city', 'retail_network')
    search_fields = ('name', 'email', 'country', 'city', 'retail_network__name')
    list_filter = ('country',)
    inlines = [ProductInline]

    def get_formsets_with_inlines(self, request, obj=None):
        for inline in self.get_inline_instances(request, obj):
            if isinstance(inline, ProductInline):
                kwargs = {
                    'fk_name': 'individual_entrepreneur',
                    'can_delete': False,
                }
                yield inline.get_formset(request, obj, **kwargs), inline

            else:
                yield inline.get_formset(request, obj), inline

admin.site.register(IndividualEntrepreneur, IndividualEntrepreneurAdmin)