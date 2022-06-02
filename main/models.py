from django.db import models
from django.urls import reverse_lazy

class Prices(models.Model):
    title = models.CharField('Услуги',max_length=100)
    price = models.IntegerField('Цена')
    cat = models.ForeignKey('Cotegory', on_delete=models.PROTECT, verbose_name='Категория')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'


class Cotegory(models.Model):
    name = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse_lazy('category', kwargs={'num_cat' : self.pk})   

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
