from tkinter.constants import CASCADE

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=20, verbose_name='name')
    price = models.FloatField(verbose_name='price')
    description = models.TextField(blank=True, verbose_name='description')
    count = models.IntegerField(verbose_name='count')
    is_active = models.BooleanField(default=False)
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        verbose_name='category'
    )

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name='name')

    def __str__(self):
        return self.name







