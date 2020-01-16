# Generated by Django 3.0.1 on 2020-01-12 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='liberi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Название')),
                ('url', models.URLField(verbose_name='Ссылка')),
                ('text', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Ссылка(библтоека)',
                'verbose_name_plural': 'Ссылки(библиотека)',
            },
        ),
        migrations.CreateModel(
            name='link_interesting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Название')),
                ('url', models.URLField(verbose_name='Ссылка')),
                ('text', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Ссылка(Это интересно)',
                'verbose_name_plural': 'Ссылки(Это интересно)',
            },
        ),
        migrations.CreateModel(
            name='link_oge_ege',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Название')),
                ('url', models.URLField(verbose_name='Ссылка')),
                ('text', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Ссылка(оге и еге)',
                'verbose_name_plural': 'Ссылки(оге и еге)',
            },
        ),
        migrations.CreateModel(
            name='link_olimpiads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Название')),
                ('url', models.URLField(verbose_name='Ссылка')),
                ('text', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Ссылка(олимпиады)',
                'verbose_name_plural': 'Ссылки(олимпиады)',
            },
        ),
        migrations.AlterField(
            model_name='caruosel',
            name='img',
            field=models.ImageField(upload_to='C:/Users/lishu/Desktop/Проект/static/images/', verbose_name='Картинка'),
        ),
        migrations.DeleteModel(
            name='link',
        ),
        migrations.DeleteModel(
            name='link_Type',
        ),
    ]
