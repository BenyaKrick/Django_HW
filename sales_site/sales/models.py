from django.core.exceptions import ValidationError
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=80, db_index=True, verbose_name="Категория")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тип аренды'
        ordering = ['title']


class Sales(models.Model):
    title = models.CharField(max_length=55, verbose_name="Заголовок объявления")
    content = models.TextField(verbose_name="Текст объявления", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name="Фотографии", blank=True)
    name_person = models.CharField(max_length=15)
    contacts = models.CharField(max_length=30, verbose_name="Контактные данные")
    price = models.IntegerField(verbose_name="Цена", null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-created_at']

    def clean(self):
        errors = {}
        if not self.content:
            errors['content'] = ValidationError(
                'Укажите описание'
            )
        if self.price and self.price < 0:
            errors['price'] = ValidationError(
                'Укажите неотрицательное значение цены'
            )
        if errors:
            raise ValidationError(errors)

    def save(
            self, force_insert=False, force_update=False,
            using=None, update_fields=None
    ):
        self.clean()
        super().save(force_insert, force_update, using, update_fields)


class Spare(models.Model):
    name = models.CharField(max_length=30)
