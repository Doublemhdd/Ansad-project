import django_filters
from .models import Wilaya, Moughataa, Commune, Product, Basket, PointOfSale, ProductPrice

# Filtre pour le modèle Wilaya
class WilayaFilter(django_filters.FilterSet):
    class Meta:
        model = Wilaya
        fields = {
            'code': ['icontains'],  # Filtre par code (insensible à la casse)
            'name': ['icontains'],  # Filtre par nom (insensible à la casse)
        }

# Filtre pour le modèle Moughataa
class MoughataaFilter(django_filters.FilterSet):
    class Meta:
        model = Moughataa
        fields = {
            'code': ['icontains'],  # Filtre par code
            'name': ['icontains'],  # Filtre par nom
            'wilaya__name': ['icontains'],  # Filtre par nom de la wilaya associée
        }

# Filtre pour le modèle Commune
class CommuneFilter(django_filters.FilterSet):
    class Meta:
        model = Commune
        fields = {
            'code': ['icontains'],  # Filtre par code
            'name': ['icontains'],  # Filtre par nom
            'moughataa__name': ['icontains'],  # Filtre par nom de la moughataa associée
        }

# Filtre pour le modèle Product
class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = {
            'name': ['icontains'],  # Filtre par nom
            'description': ['icontains'],  # Filtre par description
            'unit_measure': ['icontains'],  # Filtre par unité de mesure
            'product_type__name': ['icontains'],  # Filtre par type de produit
        }

# Filtre pour le modèle Basket
class BasketFilter(django_filters.FilterSet):
    class Meta:
        model = Basket
        fields = {
            'name': ['icontains'],  # Filtre par nom
            'description': ['icontains'],  # Filtre par description
        }

# Filtre pour le modèle PointOfSale
class PointOfSaleFilter(django_filters.FilterSet):
    class Meta:
        model = PointOfSale
        fields = {
            'name': ['icontains'],  # Filtre par nom
            'commune__name': ['icontains'],  # Filtre par nom de la commune associée
            'gps_lat': ['exact', 'gte', 'lte'],  # Filtre par latitude (exacte, supérieure ou égale, inférieure ou égale)
            'gps_lon': ['exact', 'gte', 'lte'],  # Filtre par longitude (exacte, supérieure ou égale, inférieure ou égale)
        }

# Filtre pour le modèle ProductPrice
class ProductPriceFilter(django_filters.FilterSet):
    class Meta:
        model = ProductPrice
        fields = {
            'product__name': ['icontains'],  # Filtre par nom du produit
            'point_of_sale__name': ['icontains'],  # Filtre par nom du point de vente
            'price': ['exact', 'gte', 'lte'],  # Filtre par prix (exact, supérieur ou égal, inférieur ou égal)
            'date_from': ['exact', 'gte', 'lte'],  # Filtre par date de début
            'date_to': ['exact', 'gte', 'lte'],  # Filtre par date de fin
        }