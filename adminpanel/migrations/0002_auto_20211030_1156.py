# Generated by Django 3.2.8 on 2021-10-30 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dump_json',
            old_name='Manages_json',
            new_name='manages_json',
        ),
        migrations.RenameField(
            model_name='dump_json',
            old_name='Orders_json',
            new_name='orders_json',
        ),
        migrations.RenameField(
            model_name='dump_json',
            old_name='Users_json',
            new_name='users_json',
        ),
    ]
