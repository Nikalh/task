from django.contrib import admin

from task.product.models import Product


class ProductAdmin(admin.ModelAdmin):
    """Класс, настраивающий административную панель для модели Product."""

    list_display = ('name', 'model', 'release_date', 'debt', 'created_formatted')
    list_filter = ('release_date',)
    search_fields = ('name', 'model',)

    def debt(self, obj):
        """Метод для форматирования задолженности поставщика в списке записей с двумя знаками после запятой,
        используя f-строку:."""
        return f"{obj.debt:.2f}"

    debt.short_description = "Задолженность"

    def supplier_name(self, obj):
        """Метод для отображения имени поставщика в списке записей."""

        return obj.supplier.name

    supplier_name.short_description = "Поставщик"

    def created_formatted(self, obj):
        """Метод для отображения даты создания в списке записей."""

        return obj.created_at.strftime("%Y-%m-%d %H:%M:%S")

    created_formatted.short_description = "Дата создания"


class ProductInline(admin.TabularInline):
    """Класс для отображения продуктов внутри других моделей."""

    model = Product
    extra = 0


admin.site.register(Product, ProductAdmin)
