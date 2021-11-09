from django.urls import path

from .views import (
    Account_page,
    Dump_json_page,
    Table_page,
    Search_order_page,
    Date_oder_page,
    ImportExel_page,
    ImportExelAll_page,
    SMTP_mail,
)


urlpatterns = [
    path('', Account_page.as_view(), name='account_page'),
    path('dumpjson/', Dump_json_page.as_view(), name='dumpjson_page'),
    path('table/', Table_page.as_view(), name='table_page'),
    path('searchorder/', Search_order_page.as_view(), name='searchorder_page'),
    path('dateorder/', Date_oder_page.as_view(), name='dateorder_page'),
    path('importxl/', ImportExel_page.as_view(), name='importxl_page'),
    path('importxl_all/', ImportExelAll_page.as_view(), name='importxl_all'),
    path('smtpmail/', SMTP_mail.as_view(), name='smtp_mail'),
]
