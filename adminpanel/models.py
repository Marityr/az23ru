from django.db import models
from django.db.models.fields import TextField

from django.utils import timezone


class Dump_json(models.Model):
    '''Модель для хранения json запросов'''

    orders_json = TextField(verbose_name='Заказы')
    users_json = TextField(verbose_name='Покупатели')
    manages_json = TextField(verbose_name='Менеджеры')
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Дамп Json'
        verbose_name = 'Дамп Json'
        ordering = ('published',)

    def __int__(self) -> int:
        return self.id