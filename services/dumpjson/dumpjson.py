from adminpanel.models import Orders, Product
from services.getapijson.getapijson import Wretline_json



class Json_joob:
    """Работа с json данными"""

    def save_db() -> None:
        """Получаем и сохраняем в модель данные заказов"""

        orders_json = Wretline_json.orders_json()

        for order in orders_json:
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