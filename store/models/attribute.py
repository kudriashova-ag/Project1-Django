from django.db import models
from .mixins import SlugMixin


class Attribute(SlugMixin):
    name = models.CharField('Назва', max_length=100, unique=True)

    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'
        ordering = ['name']

    def __str__(self):
        return self.name


class AttributeValue(models.Model):
    attribute = models.ForeignKey(
        Attribute,
        on_delete=models.CASCADE,
        related_name='values',
        verbose_name='Характеристика',
    )
    value = models.CharField('Значення', max_length=255)

    class Meta:
        verbose_name = 'Значення характеристики'
        verbose_name_plural = 'Значення характеристик'
        unique_together = ('attribute', 'value')

    def __str__(self):
        return f'{self.attribute.name}: {self.value}'


class ProductAttribute(models.Model):
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        related_name='attributes',
        verbose_name='Товар',
    )
    attribute_value = models.ForeignKey(
        AttributeValue,
        on_delete=models.CASCADE,
        related_name='product_attr',
        verbose_name='Значення',
    )

    class Meta:
        verbose_name = 'Характеристика товару'
        verbose_name_plural = 'Характеристики товару'
        unique_together = ('product', 'attribute_value')

    def __str__(self):
        return f'{self.product} — {self.attribute_value}'
