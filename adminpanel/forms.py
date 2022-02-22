from django import forms
from django.forms import ModelForm, TextInput, Textarea, FileInput


class Meta:
    """Метаданные формы поиска"""

    def meta(self):
        widget = {
            'number_oder': forms.TextInput(attrs={
                'class': 'form-control form-control-dark w-100',
                'type': 'text',
                'placeholder': 'Поиск по заказам'
            }),
            'date_start': forms.TextInput(attrs={
                'class': 'form-control form-control-dark w-50',
                'type': 'date',
                'placeholder': 'Начало даты',
                'style': 'float:left;'
            }),
            'date_end': forms.TextInput(attrs={
                'class': 'form-control form-control-dark w-50',
                'type': 'date',
                'placeholder': 'Конец даты',
                'style': 'float:left;'
            }),
            'search_catalog': forms.TextInput(attrs={
                'class': 'form-control form-control-dark w-100',
                'type': 'text',
                'placeholder': 'Поиск по складу',
            }),
            'user_phone_search': forms.TextInput(attrs={
                'class': 'form-control form-control-dark w-100',
                'type': 'text',
                'placeholder': 'Поиск клиента по телефону',
            }),
        }
        return widget[self]


class Search_orderForm(forms.Form):
    """Форма поиска заказа по номеру"""

    number_oder = forms.CharField(
        max_length=150, widget=Meta.meta('number_oder'))


class Datastartend_orderForm(forms.Form):
    """Форма поиска заказа по номеру"""

    date_start = forms.CharField(
        max_length=150, widget=Meta.meta('date_start'))
    date_end = forms.CharField(max_length=150, widget=Meta.meta('date_end'))


class Search_catalogForm(forms.Form):
    """Форма поиска по каталогу или вхождению"""

    search_catalog = forms.CharField(
        max_length=150, widget=Meta.meta('search_catalog'))


class Search_userForm(forms.Form):
    """Поиск информации по номеру пользователя"""

    user_phone_search = forms.CharField(
        max_length=20, widget=Meta.meta('user_phone_search')
    )
