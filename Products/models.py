from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# PRODUCT

class Product(models.Model):
    title = models.CharField('Название', max_length=50)
    description = models.TextField('Описание', max_length=300, blank=False)
    price = models.IntegerField('Цена', )
    active = models.BooleanField('Наличие', default=False, blank=True, null=True)
    slug = models.SlugField('url продукта', db_index=True, max_length=30, unique=True)
    like = models.PositiveIntegerField('Рекомендация', default=0)
    author = models.ForeignKey(User, on_delete='PROTECT', related_name='prod_author', verbose_name='Пользователь')
    image = models.ImageField('Скрин продукта')

    def get_absolute_url(self):
        return reverse('prod_detail', args=[str(self.slug)])

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

# COMMENT
