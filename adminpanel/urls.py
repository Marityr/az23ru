from django.urls import path

from .views import (
    Account_page,
    Dump_json_page,
    Table_page,
    DynamicOrdersLoad,
    Search_order_page,
    Date_oder_page,
)


urlpatterns = [
    path('', Account_page.as_view(), name='account_page'),
    path('dumpjson/', Dump_json_page.as_view(), name='dumpjson_page'),
    path('table/', Table_page.as_view(), name='table_page'),
    path('searchorder/', Search_order_page.as_view(), name='searchorder_page'),
    path('dateorder/', Date_oder_page.as_view(), name='dateorder_page'),
    path('load-more-orders/', DynamicOrdersLoad.as_view(), name='load_more_orders')
]
