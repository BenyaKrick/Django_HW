from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=80, db_index=True, verbose_name="Тип аренды")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тип аренды'
        verbose_name_plural = 'Тип аренды'
        ordering = ['title']


class Sales(models.Model):
    category = models.ForeignKey(
        'Category', on_delete=models.PROTECT, blank=True, null=True, related_name='ads',
        verbose_name="Рубрика", verbose_name_plural='Рубрики'
    )
    title = models.CharField(max_length=55, verbose_name="Заголовок объявления")
    content = models.TextField(verbose_name="Текст объявления", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name="Фотографии", blank=True)
    adress = models.TextField(verbose_name="Адрес", null=True, blank=True)
    name_person = models.CharField(max_length=15, verbose_name="ФИО")
    contacts = models.CharField(max_length=30, verbose_name="Контактные данные")
    price = models.IntegerField(verbose_name="Цена", null=True, blank=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-created_at', 'title']

    def clean(self):
        errors = {}
        if not self.content:
            errors['content'] = ValidationError(
                'Укажите описание'
            )
        if not self.adress:
            errors['adress'] = ValidationError(
                'Укажите адрес'
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
