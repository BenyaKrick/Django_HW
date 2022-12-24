from django import forms
from .models import Sales, Category
from django.core.exceptions import ValidationError


class SalesForm(forms.Form):
    title = forms.CharField(max_length=55)
    content = forms.CharField(label='Описание', widget=forms.widgets.Textarea())
    adress = forms.CharField(label='Адрес', widget=forms.widgets.Textarea())
    name_person = forms.CharField(label='ФИО', max_length=25)
    contacts = forms.CharField(label='Контактные данные', max_length=30)
    price = forms.DecimalField(label='Цена', decimal_places=2)
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label='Рубрика',
        help_text='He забудьте указать категорию объявления!',
        widget=forms.widgets.Select(attrs={'size': 8})
    )

    class Meta:
        model = Sales
        fields = ('title', 'content', 'adress', 'name_person', 'contacts', 'price', 'rubric')
