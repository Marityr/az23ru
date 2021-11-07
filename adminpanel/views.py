from django.shortcuts import redirect, render, HttpResponse
from django.views import View
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from adminpanel.models import Orders, Product

from services.jobjson.dumpjson import Json_joob
from services.importxl.importxl import Importxl

from . services.views_page import table_all
from . forms import Search_orderForm, Datastartend_orderForm


class Account_page(View):
    """Представление админ панели"""

    @staticmethod
    @login_required
    def get(request, *args, **kwargs) -> render:
        template = 'adminpanel/index.html'
        form_order_search = Search_orderForm()
        form_date = Datastartend_orderForm()
        context = {
            'title': 'AZ23RU',
            'search_order': form_order_search,
            'form_date': form_date,
        }
        return render(request, template, context)


class Dump_json_page(View):
    """Запись Json в БД"""

    @staticmethod
    @login_required
    def get(request, *args, **kwargs) -> render:
        template = 'adminpanel/dump_json.html'
        Json_joob.save_users_db()
        Json_joob.save_manager_db()
        Json_joob.save_orders_db()
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
        form_order_search = Search_orderForm()
        form_date = Datastartend_orderForm()
        orders, prod = table_all()
        context = {
            'title': 'AZ23RU',
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
            'title': 'AZ23RU',
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
            'title': 'AZ23RU',
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
            'title': 'AZ23RU',
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
            'title': 'AZ23RU',
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
        Importxl.importxl()
        context = {
            'title': 'AZ23RU',
        }

        return render(request, template, context)


class DynamicOrdersLoad(View):
    """Динамическая подгрузка заказов"""

    @staticmethod
    def get(request, *args, **kwargs) -> JsonResponse:
        pass
        # last_order_id = request.GET.get('lastOrderId')
        # more_orders = Orders.objects.filter(pk__lt=int(last_order_id))[:2]

        # if not more_orders:
        #     return JsonResponse({'data': False})

        # data = []

        # for order in more_orders:
        #     obj = {
        #         'id': order.id,
        #         'number': order.number,
        #         'id_manager': order.id_manager,
        #         'data_orders': order.data_orders,
        #     }
        #     data.append(obj)

        # data[-1]['last_order'] = True

        # return JsonResponse({'data': data})
