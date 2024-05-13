from django.contrib import admin
from django.utils.html import format_html

from network.models import NetworkObject, Product


@admin.action(description="Обнуление задолженности")
def reset_debt(modeladmin, request, queryset):
    """Очищает задолженность у выбранных объектов"""
    queryset.update(debt=0)


@admin.register(NetworkObject)
class NetworkObjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'level', 'email', 'country', 'city', 'supplier_link', 'debt', 'date_create')
    list_filter = ('city',)
    actions = [reset_debt]

    def supplier_link(self, obj):
        if obj.supplier:
            url = f"/admin/network/network-object/{obj.supplier.id}/change/"  # Прописываем url ссылки на поставщика
            return format_html(f'<a href="{url}">{obj.supplier.name}</a>')
        return "-"
    supplier_link.short_description = 'Поcтавщик'


@admin.register(Product)
class ProductsListAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'model', 'release_date',)
    list_filter = ('name',)
