from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import HttpResponse, redirect, render
from django.views import View

from adminpanel.models import Orders, Product
from services.importxl.importxl import Importxl
from services.jobjson.dumpjson import Json_joob
from services.smtp.mailsmtp import mail_smtp

from .forms import Datastartend_orderForm, Search_orderForm
from .services.views_page import table_all


class Account_page(View):
    """Представление админ панели"""

    @staticmethod
    @login_required
    def get(request, *args, **kwargs) -> render:
        template = 'adminpanel/index.html'
        form_order_search = Search_orderForm()
        form_date2 = Datastartend_orderForm()
        context = {
            'title': 'AMAXI',
            'search_order': form_order_search,
            'form_date2': form_date2,
        }
        return render(request, template, context)


class Dump_json_page(View):
    """Запись Json в БД"""

    @staticmethod
    def get(request, *args, **kwargs) -> JsonResponse:
        Json_joob.save_users_db()
        Json_joob.save_manager_db()
        Json_joob.save_orders_db()
        context = {
            'title': 'AMAXI',
            'content': "Дамп сохранен",
        }
        return JsonResponse({'data': context})


class Table_page(View):
    """Отображение Json"""

    @staticmethod
    @login_required
    def get(request, *args, **kwargs) -> render:
        template = 'adminpanel/table.html'
        form_order_search = Search_orderForm()
        form_date = Datastartend_orderForm()
        orders, prod = table_all()
        context = {
            'title': 'AMAXI',
            'orders': orders,
            'products': prod,
            'search_order': form_order_search,
            'form_date': form_date,

        }
        return render(request, template, context)


class Search_order_page(View):
    """Вывод результата поиска по номеру заказа"""

    @staticmethod
    @login_required
    def get(request, *args, **kwargs) -> render:
        template = 'adminpanel/number_order.html'
        form_order_search = Search_orderForm()
        context = {
            'title': 'AMAXI',
            'search_order': form_order_search,
        }
        return render(request, template, context)

    @staticmethod
    @login_required
    def post(request, *args, **kwargs) -> render:
        template = 'adminpanel/number_order.html'

        if request.method == 'POST':
            form = Search_orderForm(request.POST)

            if form.is_valid():
                try:
                    instance = Orders.objects.get(
                        number=form.cleaned_data['number_oder'])
                    prod = list()
                    prod.append(Product.objects.filter(
                        number_order=form.cleaned_data['number_oder']))
                    form_order_search = Search_orderForm()
                except Orders.DoesNotExist:
                    pass
        context = {
            'title': 'AMAXI',
            'order': instance,
            'products': prod,
            'search_order': form_order_search,
        }
        return render(request, template, context)


class Date_oder_page(View):
    """Вывод выборки заказов по диапазону даты"""

    @staticmethod
    @login_required
    def get(request, *args, **kwargs) -> render:
        template = 'adminpanel/number_order.html'
        form_order_search = Search_orderForm()
        context = {
            'title': 'AMAXI',
            'search_order': form_order_search,
        }
        return render(request, template, context)

    @staticmethod
    @login_required
    def post(request, *args, **kwargs) -> render:
        template = 'adminpanel/date_order.html'
        search_order = Search_orderForm()

        if request.method == 'POST':
            form = Datastartend_orderForm(request.POST)
            prod = list()

            if form.is_valid():
                try:
                    print(form.cleaned_data['date_start'], form.cleaned_data['date_end'])
                    instance = Orders.objects.filter(
                        data_orders__range=(
                            form.cleaned_data['date_start'],
                            form.cleaned_data['date_end']
                        )
                    )
                    for item in instance:
                        prod.append(Product.objects.filter(
                            number_order=item.number
                        ))
                    form_date = Datastartend_orderForm()
                except:
                    pass
        context = {
            'title': 'AMAXI',
            'orders': instance,
            'products': prod,
            'search_order': search_order,
            'form_date': form_date,
        }
        return render(request, template, context)


class ImportExel_page(View):
    """Ипротр данных в ексель"""

    @staticmethod
    @login_required
    def get(request, *args, **kwargs) -> render:
        template = 'adminpanel/import.html'
        Importxl.importxl(Orders.objects.all())
        context = {
            'title': 'AMAXI',
        }

        return render(request, template, context)


class ImportExelAll_page(View):
    """Ипротр данных в ексель"""

    @staticmethod
    @login_required
    def get(request, *args, **kwargs) -> JsonResponse:
        template = 'adminpanel/import.html'
        print('start import')
        Importxl.importxl(Orders.objects.all())
        print('end import')
        context = {
            'title': 'AMAXI',
        }

        return JsonResponse({'data': context})

    @staticmethod
    @login_required
    def post(request, *args, **kwargs) -> JsonResponse:
        if request.method == 'POST':
            tmp = request.POST
            datastart = datetime.strptime(tmp['date_start'], "%Y-%m-%d")
            dataend = datetime.strptime(tmp['date_end'], "%Y-%m-%d")
            instance = Orders.objects.filter(
                data_orders__range=(
                    datastart,
                    dataend
                )
            )
            print('start import')
            Importxl.importxl(instance)
            print('end import')

        context = {
            'title': 'AMAXI',
        }
        return JsonResponse({'data': context})


class SMTP_mail(View):
    """Отправка отчета файлом на email"""

    @staticmethod
    def get(request, *args, **kwargs) -> HttpResponse:

        Importxl.importxl(Orders.objects.all()[:2000])
        mail_smtp()
        return HttpResponse('smtp mail')


class Readexlsx(View):
    """Считывание данных из экселя и их запись в БД"""

    def get(request, *args, **kwargs) -> render:
        template = 'adminpanel/readxlsx.html'

        context = {
            'title': 'title test',
        }

        return render(request, template, context)
