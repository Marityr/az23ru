from adminpanel.models import Dump_json
from services.getapijson.getapijson import Wretline_json


def list_json() -> list:
    """Список заказов"""

    var = Wretline_json.orders_json()
    return var
