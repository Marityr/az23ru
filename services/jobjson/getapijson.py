import os
import requests


from datetime import date, datetime, timedelta
from dotenv import load_dotenv

load_dotenv()


class Wretline_json:
    """Получение json дампа"""

    def connect_api(table: str) -> str:
        """Подключение по API и получение json"""

        HOST_API = os.getenv('HOST_API')
        USER_API = os.getenv('USER_API')
        PASSWORD_API = os.getenv('PASSWORD_API')

        conect_url = f"https://{HOST_API}/cp/{table}?userlogin={USER_API}&userpsw={PASSWORD_API}&desc=true"

        return conect_url


    def orders_json() -> list:
        """Получаем json заказов"""

        response = requests.get(Wretline_json.connect_api('orders'))
        datajson = response.json()
        return datajson

    def users_json() -> list:
        """Получаем json покупателей"""

        response = requests.get(Wretline_json.connect_api('users'))
        datajson = response.json()
        return datajson
    
    def managers_json() -> list:
        """Получаем json менеджеров"""
        
        response = requests.get(Wretline_json.connect_api('managers'))
        datajson = response.json()
        return datajson

    def user_details() -> list:
        """получение данных пользователя"""
        HOST_API = os.getenv('HOST_API')
        USER_API = os.getenv('USER_API')
        PASSWORD_API = os.getenv('PASSWORD_API')

        conect_url = f"https://{HOST_API}/cp/users?userlogin={USER_API}&userpsw={PASSWORD_API}&desc=true"
        response = requests.get(conect_url)
        datajson = response.json()

        return datajson

    def pyment_user() -> list:
        """получение платежей"""

        HOST_API = os.getenv('HOST_API')
        USER_API = os.getenv('USER_API')
        PASSWORD_API = os.getenv('PASSWORD_API')

        today = date.today()
        startDate = date(today.year - 1, 1, 1)
        endDate = date(today.year - 1, 12, 31)

        conect_url = f"https://{HOST_API}/cp/finance/payments?userlogin={USER_API}&userpsw={PASSWORD_API}&createDateTimeStart={startDate}&createDateTimeEnd={endDate}"
        response = requests.get(conect_url)
        datajson = response.json()

        return datajson

    def pyment_user_this() -> list:
        """получение платежей"""

        HOST_API = os.getenv('HOST_API')
        USER_API = os.getenv('USER_API')
        PASSWORD_API = os.getenv('PASSWORD_API')

        today = date.today()
        startDate = date(today.year, 1, 1)
        endDate = date(today.year, 12, 31)

        conect_url = f"https://{HOST_API}/cp/finance/payments?userlogin={USER_API}&userpsw={PASSWORD_API}&createDateTimeStart={startDate}&createDateTimeEnd={endDate}"
        response = requests.get(conect_url)
        datajson = response.json()

        return datajson

    def vin_user(userId) -> list:
        """получение платежей"""

        HOST_API = os.getenv('HOST_API')
        USER_API = os.getenv('USER_API')
        PASSWORD_API = os.getenv('PASSWORD_API')

        id_user = userId
        conect_url = f"https://{HOST_API}/user/garage?userlogin={USER_API}&userpsw={PASSWORD_API}&userId={id_user}"
        response = requests.get(conect_url)
        datajson = response.json()

        print(conect_url)

        return datajson


    

    