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