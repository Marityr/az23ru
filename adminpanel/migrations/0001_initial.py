# Generated by Django 3.2.8 on 2021-10-24 16:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dump_json',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Orders_json', models.TextField(verbose_name='Заказы')),
                ('Users_json', models.TextField(verbose_name='Покупатели')),
                ('Manages_json', models.TextField(verbose_name='Менеджеры')),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Дамп Json',
                'verbose_name_plural': 'Дамп Json',
                'ordering': ('published',),
            },
        ),
    ]