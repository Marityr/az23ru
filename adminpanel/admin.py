from django.contrib import admin

from .models import Dump_json


class Dump_jsonAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'published',
    )


admin.site.register(Dump_json, Dump_jsonAdmin)
