from django import forms
from .models import City,Area

class SearchForm(forms.Form):
    city = forms.ModelChoiceField(
        queryset=City.objects.all(),
        empty_label='Not Specified',
        widget=forms.Select(attrs={
            "onChange": 'elementChange()'})
    )

    area = forms.ModelChoiceField(
        queryset=Area.objects.filter(city_label__label=city),
        empty_label='Not Specified'
    )

    def __str__(self):
        return self.city