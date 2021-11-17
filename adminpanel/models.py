from django.db import models
from django.db.models.fields import CharField, TextField, DateTimeField

from django.utils import timezone


class Dump_json(models.Model):
    """Модель для хранения json запросов"""

    orders_json = TextField(verbose_name='Заказы')
    users_json = TextField(verbose_name='Покупатели')
    manages_json = TextField(verbose_name='Менеджеры')
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Дамп Json'
        verbose_name = 'Дамп Json'
        ordering = ('-id',)

    def __int__(self) -> int:
        return self.id


class Orders(models.Model):
    """Данные заказа"""

    number = CharField(max_length=10, verbose_name='Номер заказа')     
    id_manager = CharField(max_length=10, verbose_name='ID менеджера')    
    data_orders = DateTimeField(verbose_name='Дата заказа')    
    price = CharField(max_length=10, verbose_name='Сумма заказа')
    paid = CharField(max_length=10, verbose_name='Оплачено')
    debt = CharField(max_length=10, verbose_name='Долг')
    name_client = CharField(max_length=50, verbose_name='Имя клиента')
    phone = CharField(max_length=10, verbose_name='Телефон')
    update_date = DateTimeField(verbose_name='Дата обновления')
    manager = CharField(max_length=50, verbose_name='Менеджер')

    class Meta:
        verbose_name_plural = 'Заказ'
        verbose_name = 'Заказы'
        ordering = ('-id',)

    def __int__(self) -> int:
        return self.id


class Product(models.Model): 
    """Позиции заказа"""

    number_order = CharField(max_length=10, verbose_name='Номер заказа')
    number_product = CharField(max_length=10, verbose_name='Номер позиции', default='')
    status = CharField(max_length=50, verbose_name='Статус')
    descriptions = CharField(max_length=250, verbose_name='Описание')
    brand = CharField(max_length=50, verbose_name='Бранд')
    article = CharField(max_length=50, verbose_name='Артикул')
    quantity = CharField(max_length=10, verbose_name='Кличество')
    price_product = CharField(max_length=10, verbose_name='Цена продажи')
    date_deadline = DateTimeField(verbose_name='Дата отгрузки')
    distributor = CharField(max_length=50, verbose_name='Дистрибьютер')
    order_distributer = CharField(max_length=50, verbose_name='Номер у дистрибьютера')
    comment = CharField(max_length=250, verbose_name='Комментарий к товару')

    class Meta:
        verbose_name_plural = 'Товар'
        verbose_name = 'Товары'
        ordering = ('id',)

    def __int__(self) -> int:
        return self.id


class Users_shop(models.Model):
    """Данные покупателя"""

    id_user = CharField(max_length=10, verbose_name='ИД покупателя')
    name = CharField(max_length=100, verbose_name='Ф.И.О')
    mobile = CharField(max_length=20, verbose_name='Номер телефона')

    class Meta:
        verbose_name_plural = 'Покупатель'
        verbose_name = 'Покупатели'
        ordering = ('-id',)

    def __int__(self) -> int:
        return self.id


class Managers_shop(models.Model):
    """Данные менеджера магазина"""

    id_manager = CharField(max_length=10, verbose_name='ИД менеджера')
    name = CharField(max_length=100, verbose_name='Ф.И.О')
    mobile = CharField(max_length=20, verbose_name='Номер телефона')

    class Meta:
        verbose_name_plural = 'Менеджер'
        verbose_name = 'Менеджеры'
        ordering = ('-id',)

    def __int__(self) -> int:
        return self.id


class Settings_user(models.Model):
    """Настройки пользователя"""

    max_table_orders = CharField(max_length=10, verbose_name='Количество отображаемых заказов по умолчанию')
    name_file = CharField(max_length=100, verbose_name='Название файлов импорта')

    class Meta:
        verbose_name_plural = 'Настройки'
        verbose_name = 'Настройки'
        ordering = ('-id',)

    def __int__(self) -> int:
        return self.id


class Number_catalog(models.Model):
    """Модель Экспорта заказов"""
    #TODO добавить поле модели для обозначения уникальности
    number_cat = CharField(max_length=20, verbose_name='Каталожный номер')
    brand = CharField(max_length=150, verbose_name='Бранд')
    descriptions = TextField(verbose_name='Описание')
    cuantity = CharField(max_length=10, verbose_name='Количество')
    price = CharField(max_length=150, verbose_name='Цена')
