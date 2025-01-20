from django import forms
from . import models


class ProductForm(forms.ModelForm):

    class Meta:
        model = models.Product
        fields = ["title", "category", "brand", "serie_number", "cost_price", "selling_price", "description"]

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "brand": forms.Select(attrs={"class": "form-control"}),
            "serie_number": forms.TextInput(attrs={"class": "form-control"}),
            "cost_price": forms.NumberInput(attrs={"class": "form-control"}),
            "selling_price": forms.NumberInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }

        labels = {
            "title": "Título",
            "category": "Categoria",
            "brand": "marca",
            "serie_number": "N° série",
            "cost_price": "Valor de custo",
            "selling_price": "Valor de venda",
            "description": "Descrição"
        }
