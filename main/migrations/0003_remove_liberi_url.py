# Generated by Django 3.0.1 on 2020-01-12 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200112_1154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='liberi',
            name='url',
        ),
    ]
