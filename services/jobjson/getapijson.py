import os
import requests

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

    