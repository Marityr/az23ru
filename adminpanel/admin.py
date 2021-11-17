from django.contrib import admin

from .models import Dump_json, Orders, Product, Users_shop, Managers_shop, Number_catalog


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
        'number_product',
        'status',
        'article',
    )
    search_fields = (
        'number_product',
    )
    #240030984


class User_shopAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'id_user',
        'name',
        'mobile'
    )


class Managers_shopAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'id_manager',
        'name',
        'mobile'
    )


class Number_catalogAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'number_cat',
        'price',
    )


admin.site.register(Number_catalog, Number_catalogAdmin)
admin.site.register(Managers_shop, Managers_shopAdmin)
admin.site.register(Users_shop, User_shopAdmin)
admin.site.register(Orders, OrdersAdmin)
admin.site.register(Product, ProdustAdmin)
admin.site.register(Dump_json, Dump_jsonAdmin)
