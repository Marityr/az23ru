from adminpanel.models import Orders, Product, Users_shop, Managers_shop
from services.jobjson.getapijson import Wretline_json


class Json_joob:
    """Работа с json данными"""

    def save_orders_db() -> None:
        """Получаем и сохраняем список заказов"""

        orders = Wretline_json.orders_json()

        for order in orders:
            print(order['number'])
            print(order['managerId'])
            print(order['date'])
            print(order['sum'])
            # TODO вывести сколько оплачено из разницы суммы и долга
            print('paid')
            print(order['debt'])
            print(order['userName'])
            # TODO запрос мобильного номера из джейсона users по id клиента
            print('mobile')
            print(order['dateUpdated'])

            for product in order['positions']:
                print(order['number'])
                print(product['status'])
                print(product['description'])
                print(product['brand'])
                print(product['numberFix'])
                print(product['quantity'])
                print(product['priceInSiteCurrency'])
                # TODO дата отгрузки (массив orders, поле date) + (массив positions, поле deadline )/24
                print('date_deadline')
                print(product['distributorName'])
                print(product['distributorOrderId'])
                print(product['comment'])

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

    def save_manager_db() -> None:
        """Получаем, сохраняем и проверяем на изменение список менеджеров"""

        managers = Wretline_json.managers_json()
        for manager in managers:
            flname = f"{manager['firstName']} {manager['lastName']}"
            manager_db = Managers_shop()
            try:
                instance = Managers_shop.objects.get(id_manager=manager['id'])
                if instance.name != flname:
                    instance.name = flname
                if instance.mobile != manager['mobile']:
                    if manager['mobile'] == None:
                        instance.mobile = ' '
                    else:
                        instance.mobile = manager['mobile']
                instance.save()
            except Managers_shop.DoesNotExist:
                manager_db.id_manager = manager['id']
                manager_db.name = flname
                if manager['mobile'] == None:
                    manager_db.mobile = ' '
                else:
                    manager_db.mobile = manager['mobile']
                manager_db.save()
