# Generated by Django 2.2.6 on 2019-12-13 03:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laporan', '0009_auto_20191213_1042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='laporan',
            name='kategori',
        ),
    ]
