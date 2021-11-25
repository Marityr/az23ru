from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import HttpResponse, redirect, render
from django.views import View

from adminpanel.models import Orders, Product, Number_catalog
from services.importxl.importxl import Importxl
from services.jobjson.dumpjson import Json_joob
from services.smtp.mailsmtp import mail_smtp
from services.exportxlsx.exportxlsx import Export_file

from .forms import Datastartend_orderForm, Search_orderForm, Search_catalogForm
from .services.views_page import table_all


class Account_page(View):
    """Представление админ панели"""

    @staticmethod
    @login_required
    def get(request, *args, **kwargs) -> render:
        template = 'adminpanel/index.html'
        form_order_search = Search_orderForm()
        form_date2 = Datastartend_orderForm()
        form_catalog = Search_catalogForm()
        context = {
            'title': 'AMAXI',
            'search_order': form_order_search,
            'form_date2': form_date2,
            'form_catalog': form_catalog,
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
        form_catalog = Search_catalogForm()
        orders, prod = table_all()
        context = {
            'title': 'AMAXI',
            'orders': orders,
            'products': prod,
            'search_order': form_order_search,
            'form_date': form_date,
            'form_catalog': form_catalog,
        }
        return render(request, template, context)


class Search_order_page(View):
    """Вывод результата поиска по номеру заказа, номеру телефона с вхождением либо артиклу позиции с вхождением"""

    @staticmethod
    @login_required
    def get(request, *args, **kwargs) -> render:
        template = 'adminpanel/number_order.html'
        form_order_search = Search_orderForm()
        form_catalog = Search_catalogForm()
        context = {
            'title': 'AMAXI',
            'search_order': form_order_search,
            'form_catalog': form_catalog,
        }
        return render(request, template, context)

    @staticmethod
    @login_required
    def post(request, *args, **kwargs) -> render:
        form_catalog = Search_catalogForm()

        if request.method == 'POST':
            form = Search_orderForm(request.POST)
            if form.is_valid():
                number_oder = form.cleaned_data['number_oder']
        try:
            template = 'adminpanel/number_order.html'
            Product.objects.filter(article__icontains=number_oder)
            product = Product.objects.filter(article__icontains=number_oder)
            tpm = set(product.values_list("number_order", flat=True))
            instance = Orders.objects.filter(number__in=tpm)

            prod = list()
            for item in instance:
                prod.append(Product.objects.filter(number_order=item.number))
            form_order_search = Search_orderForm()
            context = {
                'title': 'AMAXI',
                'orders': instance,
                'products': prod,
                'search_order': form_order_search,
                'form_catalog': form_catalog,
            }
            
            if not instance:
                template = 'adminpanel/phone_order.html'
                Orders.objects.filter(phone__icontains=number_oder)
                instance = Orders.objects.filter(phone__icontains=number_oder)[:50]
                prod = list()
                for item in instance:
                    prod.append(Product.objects.filter(number_order=item.number))
                form_order_search = Search_orderForm()
                context = {
                    'title': 'AMAXI',
                    'orders': instance,
                    'products': prod,
                    'search_order': form_order_search,
                    'form_catalog': form_catalog,
                }
                if not instance:
                    return redirect('nonesearch_page')
            return render(request, template, context)
        except Product.DoesNotExist:
            # TODO переделать поиск по номеру телефона с вхождением на несколько заказов
            try:
                template = 'adminpanel/phone_order.html'
                Orders.objects.filter(phone__icontains=number_oder)
                instance = Orders.objects.filter(phone__icontains=number_oder)[:100]
                prod = list()
                for item in instance:
                    prod.append(Product.objects.filter(number_order=item.number))
                form_order_search = Search_orderForm()
                context = {
                    'title': 'AMAXI',
                    'orders': instance,
                    'products': prod,
                    'search_order': form_order_search,
                    'form_catalog': form_catalog,
                }
                if not instance:
                    return redirect('nonesearch_page')
            except Orders.DoesNotExist:
                return redirect('nonesearch_page')

        print(template)
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
                    print(form.cleaned_data['date_start'],
                          form.cleaned_data['date_end'])
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
                except Orders.DoesNotExist:
                    redirect('nonesearch_page')
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


class Exportdata_page(View):
    """Инициация считывания данных"""

    @staticmethod
    @login_required
    def get(request, *args, **kwargs) -> HttpResponse:

        Export_file.read_data()

        return HttpResponse('read data')


class Searchcatalog_page(View):
    """Поиск по каталогу или вхождению"""

    @staticmethod
    @login_required
    def get(request, *args, **kwargs) -> render:
        template = 'adminpanel/searchcatalog.html'
        form_order_search = Search_orderForm()
        form_date2 = Datastartend_orderForm()
        form_catalog = Search_catalogForm()
        context = {
            'title': 'AMAXI',
            'search_order': form_order_search,
            'form_date2': form_date2,
            'form_catalog': form_catalog,
        }
        return render(request, template, context)

    @staticmethod
    @login_required
    def post(request, *args, **kwargs) -> render:
        template = 'adminpanel/searchcatalog.html'

        data_form = Search_catalogForm(request.POST)

        if data_form.is_valid():
            search_catalog = data_form.cleaned_data['search_catalog']

        try:
            Number_catalog.objects.get(number_cat=search_catalog)
            instanse = Number_catalog.objects.filter(number_cat=search_catalog)
        except Number_catalog.DoesNotExist:
            try:
                Number_catalog.objects.filter(
                    descriptions__icontains=search_catalog)
                instanse = Number_catalog.objects.filter(
                    descriptions__icontains=search_catalog)
                # TODO проверить логку исключения при поиске с вхождением
                if not instanse:
                    return redirect('nonesearch_page')
            except Number_catalog.DoesNotExist:
                return redirect('nonesearch_page')

        form_order_search = Search_orderForm()
        form_catalog = Search_catalogForm()
        context = {
            'title': 'AMAXI',
            'search_order': form_order_search,
            'form_catalog': form_catalog,
            'instanse': instanse,
        }

        return render(request, template, context)


class NoneSearch_page(View):
    """Поиск не дал результатов"""

    @staticmethod
    @login_required
    def get(request, *args, **kwargs) -> render:
        template = 'adminpanel/404_search.html'
        form_order_search = Search_orderForm()
        form_date2 = Datastartend_orderForm()
        form_catalog = Search_catalogForm()
        context = {
            'title': 'AMAXI',
            'search_order': form_order_search,
            'form_date2': form_date2,
            'form_catalog': form_catalog,
        }
        return render(request, template, context)
