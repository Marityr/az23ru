# Generated by Django 3.2.8 on 2021-11-03 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0003_auto_20211102_1611'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users_shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.CharField(max_length=10, verbose_name='ИД покупателя')),
                ('name', models.CharField(max_length=100, verbose_name='Ф.И.О')),
                ('mobile', models.CharField(max_length=20, verbose_name='Номер телефона')),
            ],
            options={
                'verbose_name': 'Покупатели',
                'verbose_name_plural': 'Покупатель',
                'ordering': ('-id',),
            },
        ),
        migrations.AlterField(
            model_name='product',
            name='date_deadline',
            field=models.DateTimeField(verbose_name='Дата отгрузки'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price_product',
            field=models.CharField(max_length=10, verbose_name='Цена продажи'),
        ),
    ]
