from adminpanel.models import Dump_json


def list_json() -> None:
    last_json = Dump_json.objects.last()
    print(last_json)