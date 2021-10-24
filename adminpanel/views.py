from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required

from services.getapijson.getapijson import Wretline_json


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
        users = Wretline_json.managers_json()
        context = {
            'title': 'AZ23RU',
            'users': users['resellerId'],
        }
        return render(request, template, context)