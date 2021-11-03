from adminpanel.models import Orders, Product, Users_shop
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
            #TODO вывести сколько оплачено из разницы суммы и долга
            print('paid')
            print(order['debt'])
            print(order['userName'])
            #TODO запрос мобильного номера из джейсона users по id клиента
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
                #TODO дата отгрузки (массив orders, поле date) + (массив positions, поле deadline )/24
                print('date_deadline')
                print(product['distributorName'])
                print(product['distributorOrderId'])
                print(product['comment'])

    def  save_users_db() -> None:
        """Получаем и сохраняем список покупателей"""

        #TODO проверка и сохранение дамба пользователей
        users = Wretline_json.users_json()

        for user in users:
            user_db = Users_shop()
            try:
                instance = Users_shop.objects.get(id_user = user['userId'])
            except Users_shop.DoesNotExist:
                user_db.id_user = user['userId']
                user_db.name = user['name']
                user_db.mobile = user['mobile']
                user_db.save()
            else:
                print ("Not Found")

            #print(user['userId'], user['name'], user['mobile'])

    def examitation(tmp: str, tmp_two: str) -> bool:
        """Проверка соответствия записей в дейсоне и БД"""

        if tmp == tmp_two:
            return True
        else:
            return False

        