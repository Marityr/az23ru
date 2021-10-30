from django.urls import path

from .views import Account_page, Dump_json_page, Table_page


urlpatterns = [
    path('', Account_page.as_view(), name='account_page'),
    path('dumpjson/', Dump_json_page.as_view(), name='dumpjson_page'),
    path('table/', Table_page.as_view(), name='table_page'),
]