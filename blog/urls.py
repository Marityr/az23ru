from django.urls import path, include

from .views import LoginFormView


urlpatterns = [
    path('', LoginFormView.as_view(), name='login_page'),
    path('', include('django.contrib.auth.urls'))
]