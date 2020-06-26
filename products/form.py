from django import forms
from .models import Product

class ProductForm(forms.ModelForm):

     title = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter title'}))
     description = forms.CharField(widget = forms.Textarea(attrs={'class':'form-control','placeholder': 'Enter description'}))
     price = forms.DecimalField(initial = 0.0)

     class Meta:
          model = Product
          fields = ['title', 'description', 'price']


class SearchForm(forms.Form):

     search = forms.CharField(max_length=200)