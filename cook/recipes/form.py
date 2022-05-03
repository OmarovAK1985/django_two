from django import forms


class form_for_number(forms.Form):
    count = forms.IntegerField(label='Для подсчета количества ингредиентов введите число')
