from django.contrib import admin

from .models import Dump_json, Orders, Product


class Dump_jsonAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'published',
    )


class OrdersAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'number',
        'data_orders',
        'update_date',
    )


class ProdustAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'number_order',
        'status',
        'article',
    )


admin.site.register(Orders, OrdersAdmin)
admin.site.register(Product, ProdustAdmin)
admin.site.register(Dump_json, Dump_jsonAdmin)
