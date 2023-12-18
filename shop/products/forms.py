from django import forms

class AddProduct(forms.Form):
    name = forms.CharField(max_length=20)
    description = forms.CharField(max_length=360)
    price = forms.IntegerField()