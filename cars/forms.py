from django import forms
from cars.models import Car 

class carsModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = 'model', 'brand', 'factory_year', 'model_year', 'plate', 'purchase_value', 'sale_value', 'photos'
    
    def clean_value(self):
        value = self.cleaned_data.get('sale_value')
        print(value)
        if value <= 0:
            self.add_error('value', 'O valor não pode ser negativo.')
        return value