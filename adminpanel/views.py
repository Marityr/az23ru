from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required


class Account_page(View):
    """Представление админ панели"""

    @staticmethod
    @login_required
    def get(request, *args, **kwargs) -> render:
        template = 'adminpanel/index.html'
        context = {'title': 'adminpanel'}
        return render(request, template, context)