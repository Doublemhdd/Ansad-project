from django import forms
from .models import *
# Formulaire pour Moughataa
class MoughataaForm(forms.ModelForm):
    class Meta:
        model = Moughataa
        fields = ['code', 'name', 'wilaya']

# Formulaire pour Wilaya
class WilayaForm(forms.ModelForm):
    class Meta:
        model = Wilaya
        fields = ['code', 'name']

# Formulaire pour Commune
class CommuneForm(forms.ModelForm):
    class Meta:
        model = Commune
        fields = ['code', 'name', 'moughataa']

# Formulaire pour Product
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['code', 'name', 'description', 'unit_measure', 'product_type']  # Ajout de 'code'

# Formulaire pour Basket
class BasketForm(forms.ModelForm):
    class Meta:
        model = Basket
        fields = ['code', 'name', 'description']  # Ajout de 'code'

# Formulaire pour ProductPrice
class ProductPriceForm(forms.ModelForm):
    class Meta:
        model = ProductPrice
        fields = ['product', 'point_of_sale', 'price', 'date_from', 'date_to']

# Formulaire pour PointOfSale
class PointOfSaleForm(forms.ModelForm):
    class Meta:
        model = PointOfSale
        fields = ['code', 'name', 'type', 'commune', 'gps_lat', 'gps_lon']  # Ajout de 'code' et 'type'

# Formulaire pour BasketProduct
class BasketProductForm(forms.ModelForm):
    class Meta:
        model = BasketProduct
        fields = ['basket', 'product', 'weight', 'date_from', 'date_to']  # Ajout de 'date_from' et 'date_to'
# Formilaire pour ProductType
class ProductTypeForm(forms.ModelForm):
    class Meta:
        model = ProductType
        fields = ['code', 'name', 'description']
# Filtres
class WilayaFilterForm(forms.Form):
    code = forms.CharField(label='Code', required=False)
    name = forms.CharField(label='Nom', required=False)

class ProductPriceFilterForm(forms.Form):
    product = forms.CharField(label='Produit', required=False)
    point_of_sale = forms.CharField(label='Point de vente', required=False)
    price_min = forms.DecimalField(label='Prix minimum', required=False)
    price_max = forms.DecimalField(label='Prix maximum', required=False)
    date_from = forms.DateField(label='Date de début', required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    date_to = forms.DateField(label='Date de fin', required=False, widget=forms.DateInput(attrs={'type': 'date'}))