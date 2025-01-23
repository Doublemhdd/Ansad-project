from django import forms
from .models import Moughataa

class MoughataaForm(forms.ModelForm):
    class Meta:
        model = Moughataa
        fields = ['code', 'name', 'wilaya']

from django import forms
from .models import Wilaya

class WilayaForm(forms.ModelForm):
    class Meta:
        model = Wilaya
        fields = ['code', 'name']

from django import forms
from .models import Commune

class CommuneForm(forms.ModelForm):
    class Meta:
        model = Commune
        fields = ['code', 'name', 'moughataa']

from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'unit_measure', 'product_type']

from django import forms
from .models import Basket

class BasketForm(forms.ModelForm):
    class Meta:
        model = Basket
        fields = ['name', 'description']

from django import forms
from .models import ProductPrice

class ProductPriceForm(forms.ModelForm):
    class Meta:
        model = ProductPrice
        fields = ['product', 'point_of_sale', 'price', 'date_from', 'date_to']
from django import forms
from .models import PointOfSale

class PointOfSaleForm(forms.ModelForm):
    class Meta:
        model = PointOfSale
        fields = ['name', 'commune', 'gps_lat', 'gps_lon']

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