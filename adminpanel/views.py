from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required

from services.dumpjson.dumpjson import save_dump
from services.listjson.listjson import list_json


class Account_page(View):
    """Представление админ панели"""

    @staticmethod
    @login_required
    def get(request, *args, **kwargs) -> render:
        template = 'adminpanel/index.html'
        context = {'title': 'AZ23RU'}
        return render(request, template, context)


class Dump_json_page(View):
    """Запись Json в БД"""

    @staticmethod
    @login_required
    def get(request, *args, **kwargs) -> render:
        template = 'adminpanel/dump_json.html'
        save_dump()
        context = {
            'title': 'AZ23RU',
            'content': "Дамп сохранен",
        }
        return render(request, template, context)


class Table_page(View):
    """Запись Json в БД"""

    @staticmethod
    @login_required
    def get(request, *args, **kwargs) -> render:
        template = 'adminpanel/table.html'
        #orders = list_json()
        list_json()
        context = {
            'title': 'AZ23RU',
            'order': "1",
        }
        return render(request, template, context)