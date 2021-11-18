from django import forms
from django.forms import ModelForm, TextInput, Textarea, FileInput


class Meta:
    """Метаданные формы поиска"""

    def meta(self):
        widget = {
            'number_oder': forms.TextInput(attrs={
                'class': 'form-control form-control-dark w-100',
                'type': 'text',
                'placeholder': 'Поиск по № заказа'
            }),
            'date_start': forms.TextInput(attrs={
                'class': 'form-control form-control-dark w-50',
                'type': 'date',
                'placeholder': 'Поиск по № заказа',
                'style': 'float:left;'
            }),
            'date_end': forms.TextInput(attrs={
                'class': 'form-control form-control-dark w-50',
                'type': 'date',
                'placeholder': 'Поиск по № заказа',
                'style': 'float:left;'
            }),
            'search_catalog': forms.TextInput(attrs={
                'class': 'form-control form-control-dark w-100',
                'type': 'text',
                'placeholder': 'Поиск по каталогу',
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
