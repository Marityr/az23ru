from django import db

from adminpanel.models import Orders, Product, Users_shop, Managers_shop
from services.jobjson.getapijson import Wretline_json

import datetime


class Json_joob:
    """Работа с json данными"""

    def save_orders_db() -> None:
        """Получаем, сохраняем и проверяем данные по заказу"""
        # TODO уменьшить количество обращений к БД
        orders = Wretline_json.orders_json()

        #Orders.objects.all().delete()
        #Product.objects.all().delete()
        
        for order in orders:
            orders_db = Orders()

            try:
                instance = Orders.objects.get(
                    number=order['number'])
                Json_joob.save_midel_order(instance, order)
            except Orders.DoesNotExist:
                Json_joob.save_midel_order(orders_db, order)

            for product in order['positions']:
                products_db = Product()

                print(product['id'])
                try:
                    instance = Product.objects.get(
                        number_order=order['number'],
                        number_product=product['id']
                    )
                    instance.status = product['status']
                    instance.comment = product['comment']
                    instance.save()
                except Product.DoesNotExist:
                    order_nubmer =order['number']
                    Json_joob.save_model_product(
                        products_db,
                        order_nubmer,
                        order['date'],
                        product)
            db.connections.close_all()

    def save_users_db() -> None:
        """Получаем и сохраняем список покупателей"""

        users = Wretline_json.users_json()

        for user in users:
            user_db = Users_shop()

            try:
                instance = Users_shop.objects.get(id_user=user['userId'])

                if instance.name != user['name']:
                    instance.name = user['name']
                if instance.mobile != user['mobile']:
                    instance.mobile = user['mobile']
                instance.save()
            except Users_shop.DoesNotExist:
                user_db.id_user = user['userId']
                user_db.name = user['name']
                user_db.mobile = user['mobile']
                user_db.save()
            db.connections.close_all()

    def save_manager_db() -> None:
        """Получаем, сохраняем и проверяем на изменение список менеджеров"""

        managers = Wretline_json.managers_json()

        for manager in managers:
            flname = f"{manager['firstName']} {manager['lastName']}"
            manager_db = Managers_shop()

            try:
                instance = Managers_shop.objects.get(
                    id_manager=manager['contractorId'])
                if instance.name != flname:
                    instance.name = flname
                if instance.mobile != manager['mobile']:
                    if manager['mobile'] == None:
                        instance.mobile = ' '
                    else:
                        instance.mobile = manager['mobile']
                instance.save()
            except Managers_shop.DoesNotExist:
                manager_db.id_manager = manager['contractorId']
                manager_db.name = flname
                if manager['mobile'] == None:
                    manager_db.mobile = ' '
                else:
                    manager_db.mobile = manager['mobile']
                manager_db.save()
            db.connections.close_all()

    def save_midel_order(orders_db, order) -> None:
        """Сохраняем данные заказов"""
        
        paid = order['sum'] - int(float(order['debt']))

        orders_db.number = order['number']
        orders_db.id_manager = Json_joob.managernumber(Json_joob.manager_name(order['userId']))
        orders_db.data_orders = order['date']
        orders_db.price = Json_joob.split_position(order['sum'])
        orders_db.debt = Json_joob.split_position(int(float(order['debt'])))
        orders_db.paid = Json_joob.split_position(paid)
        orders_db.name_client = order['userName']
        orders_db.phone = Json_joob.mobile_user(order['userId'])
        orders_db.update_date = order['dateUpdated']
        orders_db.manager = Json_joob.manager_name(order['userId'])
        orders_db.save()

    def mobile_user(userid) -> str:
        """Получаем номер телефона"""

        mobile = ''
        try:
            instance = Users_shop.objects.get(id_user=userid)
            if instance.mobile == '':
                mobile = '----------'
            else:
                mobile = instance.mobile
        except:
            instance = Managers_shop.objects.get(id_manager=userid)
            if instance.mobile == '':
                mobile = '----------'
            else:
                mobile = instance.mobile
        return mobile

    def manager_name(userid) -> str:
        """Получаем имя сотрудника"""

        name = ''
        try:
            instance = Managers_shop.objects.get(id_manager=userid)
            name = instance.name
        except:
            name = '----------'
        return name

    def save_model_product(products_db, number, data_order, product) -> None:
        """Сохраняем проверенные данные товаров"""

        products_db.number_order = number
        products_db.number_product = product['id']
        products_db.status = product['status']
        products_db.descriptions = product['description']
        products_db.brand = product['brand']
        products_db.article = product['numberFix']
        products_db.quantity = product['quantity']
        products_db.price_product = Json_joob.split_position(int(float(product['priceInSiteCurrency'])))
        products_db.date_deadline = Json_joob.time_add(
            data_order,
            product['deadline'])
        products_db.distributor = product['distributorName']
        if product['distributorOrderId'] == None:
            products_db.order_distributer = ' '
        else:
            products_db.order_distributer = product['distributorOrderId']
        products_db.comment = product['comment']
        products_db.save()

    def time_add(date_order, add_hour) -> str:
        """Дата поставки"""

        date_object = datetime.datetime.strptime(
            date_order, '%Y-%m-%d %H:%M:%S')
        duration_minutes = datetime.timedelta(hours=int(add_hour))
        result = date_object + duration_minutes
        return result

    def split_position(price) -> int:
        """Сплит цены по разрядам"""

        z = '{0:,}'.format(int(float(price))).replace(',', ' ')
        return z

    def dashinsert(str) -> str:
        """Сплит номера заказа"""

        midPoint = len(str)//2
        return str[:midPoint] + '-' + str[midPoint:]

    def managernumber(manager) -> str:
        number_id = 0
        if manager == 'Валентин Панаетидис':
            number_id = 1
        if manager == 'Василий Панаетидис':
            number_id = 2
        if manager == 'Максим Паненко':
            number_id = 3
        if manager == 'Роман Оробейко':
            number_id = 4
        if manager == 'Дмитрий Маслов':
            number_id = 5
        if manager == 'Сергей Параскевопуло':
            number_id = 6
        if manager == 'Станислав Ефремов':
            number_id = 7
        
        return number_id
