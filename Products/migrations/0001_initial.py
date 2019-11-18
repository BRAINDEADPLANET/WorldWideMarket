# Generated by Django 2.2.7 on 2019-11-18 08:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.TextField(max_length=300, verbose_name='Описание')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('active', models.BooleanField(blank=True, default=False, null=True, verbose_name='Наличие')),
                ('slug', models.SlugField(max_length=30, unique=True, verbose_name='url продукта')),
                ('like', models.PositiveIntegerField(default=0, verbose_name='Рекомендация')),
                ('image', models.ImageField(upload_to='', verbose_name='Скрин продукта')),
                ('author', models.ForeignKey(on_delete='PROTECT', related_name='prod_author', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]
