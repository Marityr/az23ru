from django.urls import path

from .views import Account_page, Dump_json_page


urlpatterns = [
    path('', Account_page.as_view(), name='account_page'),
    path('dumpjson/', Dump_json_page.as_view(), name='dumpjson_page'),
]