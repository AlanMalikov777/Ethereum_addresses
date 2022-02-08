from django import forms
from . models import Ether

class ProductForm(forms.ModelForm):
    class Meta:
        model = Ether
        fields = '__all__'
        widgets = {
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'num_of_products': forms.TextInput(attrs={'class': 'form-control'}),
        }
