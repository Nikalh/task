from django.contrib import admin

from task.factory.models import Factory
from task.product.admin import ProductInline


class FactoryAdmin(admin.ModelAdmin):
    """Класс настраивающий административную панель для модели фабрик."""
    list_display = ('name', 'email', 'country', 'city')
    search_fields = ('name', 'email', 'country', 'city')
    inlines = [ProductInline]

    def get_formsets_with_inlines(self, request, obj=None):
        """Метод для управления отображением inline-форм в административной панели."""
        for inline in self.get_inline_instances(request, obj):
            if isinstance(inline, ProductInline):
                kwargs = {
                    'fk_name': 'factory',
                    'can_delete': False,
                }
                yield inline.get_formset(request, obj, **kwargs), inline

            else:
                yield inline.get_formset(request, obj), inline

admin.site.register(Factory, FactoryAdmin)