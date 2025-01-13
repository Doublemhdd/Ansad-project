from django.shortcuts import render, get_object_or_404, redirect
from .models import Moughataa
from .forms import MoughataaForm
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Wilaya
from .forms import WilayaForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Commune
from .forms import CommuneForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Basket
from .forms import BasketForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import ProductPrice
from .forms import ProductPriceForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import PointOfSale
from .forms import PointOfSaleForm

# Liste des points de vente
def point_of_sale_list(request):
    points_of_sale = PointOfSale.objects.all()
    return render(request, 'point_of_sale_list.html', {'points_of_sale': points_of_sale})

# Créer un point de vente
def point_of_sale_create(request):
    if request.method == 'POST':
        form = PointOfSaleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('point_of_sale_list')
    else:
        form = PointOfSaleForm()
    return render(request, 'point_of_sale_form.html', {'form': form})

# Modifier un point de vente
def point_of_sale_update(request, pk):
    point_of_sale = get_object_or_404(PointOfSale, pk=pk)
    if request.method == 'POST':
        form = PointOfSaleForm(request.POST, instance=point_of_sale)
        if form.is_valid():
            form.save()
            return redirect('point_of_sale_list')
    else:
        form = PointOfSaleForm(instance=point_of_sale)
    return render(request, 'point_of_sale_form.html', {'form': form})

# Supprimer un point de vente
def point_of_sale_delete(request, pk):
    point_of_sale = get_object_or_404(PointOfSale, pk=pk)
    if request.method == 'POST':
        point_of_sale.delete()
        return redirect('point_of_sale_list')
    return render(request, 'point_of_sale_confirm_delete.html', {'point_of_sale': point_of_sale})
# Liste des prix
def price_list(request):
    prices = ProductPrice.objects.all()
    return render(request, 'price_list.html', {'prices': prices})

# Créer un prix
def price_create(request):
    if request.method == 'POST':
        form = ProductPriceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('price_list')
    else:
        form = ProductPriceForm()
    return render(request, 'price_form.html', {'form': form})

# Modifier un prix
def price_update(request, pk):
    price = get_object_or_404(ProductPrice, pk=pk)
    if request.method == 'POST':
        form = ProductPriceForm(request.POST, instance=price)
        if form.is_valid():
            form.save()
            return redirect('price_list')
    else:
        form = ProductPriceForm(instance=price)
    return render(request, 'price_form.html', {'form': form})

# Supprimer un prix
def price_delete(request, pk):
    price = get_object_or_404(ProductPrice, pk=pk)
    if request.method == 'POST':
        price.delete()
        return redirect('price_list')
    return render(request, 'price_confirm_delete.html', {'price': price})

# Liste des paniers
def basket_list(request):
    baskets = Basket.objects.all()
    return render(request, 'basket_list.html', {'baskets': baskets})

# Créer un panier
def basket_create(request):
    if request.method == 'POST':
        form = BasketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('basket_list')
    else:
        form = BasketForm()
    return render(request, 'basket_form.html', {'form': form})

# Modifier un panier
def basket_update(request, pk):
    basket = get_object_or_404(Basket, pk=pk)
    if request.method == 'POST':
        form = BasketForm(request.POST, instance=basket)
        if form.is_valid():
            form.save()
            return redirect('basket_list')
    else:
        form = BasketForm(instance=basket)
    return render(request, 'basket_form.html', {'form': form})

# Supprimer un panier
def basket_delete(request, pk):
    basket = get_object_or_404(Basket, pk=pk)
    if request.method == 'POST':
        basket.delete()
        return redirect('basket_list')
    return render(request, 'basket_confirm_delete.html', {'basket': basket})

# Liste des produits
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

# Créer un produit
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})

# Modifier un produit
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_form.html', {'form': form})

# Supprimer un produit
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'product_confirm_delete.html', {'product': product})

# Liste des communes
def commune_list(request):
    communes = Commune.objects.all()
    return render(request, 'commune_list.html', {'communes': communes})

# Créer une commune
def commune_create(request):
    if request.method == 'POST':
        form = CommuneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('commune_list')
    else:
        form = CommuneForm()
    return render(request, 'commune_form.html', {'form': form})

# Modifier une commune
def commune_update(request, pk):
    commune = get_object_or_404(Commune, pk=pk)
    if request.method == 'POST':
        form = CommuneForm(request.POST, instance=commune)
        if form.is_valid():
            form.save()
            return redirect('commune_list')
    else:
        form = CommuneForm(instance=commune)
    return render(request, 'commune_form.html', {'form': form})

# Supprimer une commune
def commune_delete(request, pk):
    commune = get_object_or_404(Commune, pk=pk)
    if request.method == 'POST':
        commune.delete()
        return redirect('commune_list')
    return render(request, 'commune_confirm_delete.html', {'commune': commune})

# Liste des wilayas
def wilaya_list(request):
    wilayas = Wilaya.objects.all()
    return render(request, 'wilaya_list.html', {'wilayas': wilayas})

# Créer une wilaya
def wilaya_create(request):
    if request.method == 'POST':
        form = WilayaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('wilaya_list')
    else:
        form = WilayaForm()
    return render(request, 'wilaya_form.html', {'form': form})

# Modifier une wilaya
def wilaya_update(request, pk):
    wilaya = get_object_or_404(Wilaya, pk=pk)
    if request.method == 'POST':
        form = WilayaForm(request.POST, instance=wilaya)
        if form.is_valid():
            form.save()
            return redirect('wilaya_list')
    else:
        form = WilayaForm(instance=wilaya)
    return render(request, 'wilaya_form.html', {'form': form})

# Supprimer une wilaya
def wilaya_delete(request, pk):
    wilaya = get_object_or_404(Wilaya, pk=pk)
    if request.method == 'POST':
        wilaya.delete()
        return redirect('wilaya_list')
    return render(request, 'wilaya_confirm_delete.html', {'wilaya': wilaya})

def home(request):
    return render(request, 'home.html')

# Liste des moughataas
def moughataa_list(request):
    moughataas = Moughataa.objects.all()
    return render(request, 'moughataa_list.html', {'moughataas': moughataas})

# Créer un moughataa
def moughataa_create(request):
    if request.method == 'POST':
        form = MoughataaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('moughataa_list')
    else:
        form = MoughataaForm()
    return render(request, 'moughataa_form.html', {'form': form})

# Modifier un moughataa
def moughataa_update(request, pk):
    moughataa = get_object_or_404(Moughataa, pk=pk)
    if request.method == 'POST':
        form = MoughataaForm(request.POST, instance=moughataa)
        if form.is_valid():
            form.save()
            return redirect('moughataa_list')
    else:
        form = MoughataaForm(instance=moughataa)
    return render(request, 'moughataa_form.html', {'form': form})

# Supprimer un moughataa
def moughataa_delete(request, pk):
    moughataa = get_object_or_404(Moughataa, pk=pk)
    if request.method == 'POST':
        moughataa.delete()
        return redirect('moughataa_list')
    return render(request, 'moughataa_confirm_delete.html', {'moughataa': moughataa})