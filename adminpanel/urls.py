from django.urls import path

from .views import Account_page


urlpatterns = [
    path('', Account_page.as_view(), name='account_page'),
]