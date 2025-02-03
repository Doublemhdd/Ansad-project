from django.db import models

# Structures administratives
class Wilaya(models.Model):
    code = models.CharField(max_length=45)
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name

class Moughataa(models.Model):
    code = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    wilaya = models.ForeignKey(Wilaya, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
# Communes
class Commune(models.Model):
    code = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    moughataa = models.ForeignKey(Moughataa, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Produits
class ProductType(models.Model):
    code = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    description = models.TextField()

    def __str__(self):
        return self.name

class Product(models.Model):
    code = models.CharField(max_length=45)  # Ajouté
    name = models.CharField(max_length=45)
    description = models.TextField()
    unit_measure = models.CharField(max_length=45)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Panier de produits
class Basket(models.Model):
    code = models.CharField(max_length=45, default="DEFAULT_CODE")
    name = models.CharField(max_length=45)
    description = models.TextField()

    def __str__(self):
        return self.name


class BasketProduct(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    weight = models.FloatField()
    date_from = models.DateField()  # Ajouté
    date_to = models.DateField()  # Ajouté

    def __str__(self):
        return f"{self.basket.name} - {self.product.name}"

# Points de vente
class PointOfSale(models.Model):
    code = models.CharField(max_length=45)  # Ajouté
    name = models.CharField(max_length=45)
    type = models.CharField(max_length=45)  # Ajouté
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE)
    gps_lat = models.FloatField()
    gps_lon = models.FloatField()

    def __str__(self):
        return self.name

class ProductPrice(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    point_of_sale = models.ForeignKey(PointOfSale, on_delete=models.CASCADE)
    price = models.FloatField()
    date_from = models.DateField()
    date_to = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.product.name} - {self.point_of_sale.name}"