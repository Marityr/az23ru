from adminpanel.models import Dump_json
from services.getapijson.getapijson import Wretline_json

def save_dump() -> None:
    new_dump = Dump_json()
    new_dump.orders_json = Wretline_json.orders_json()
    new_dump.users_json = Wretline_json.users_json()
    new_dump.manages_json = Wretline_json.managers_json()
    new_dump.save()