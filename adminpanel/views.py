from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required

from services.jobjson.dumpjson import Json_joob


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
        Json_joob.save_users_db()
        context = {
            'title': 'AZ23RU',
            'content': "Дамп сохранен",
        }
        return render(request, template, context)


class Table_page(View):
    """Отображение Json"""

    @staticmethod
    @login_required
    def get(request, *args, **kwargs) -> render:
        template = 'adminpanel/table.html'
        context = {
            'title': 'AZ23RU',
        }
        return render(request, template, context)