from django.shortcuts import render, get_object_or_404, redirect
from .models import Moughataa
from .forms import MoughataaForm
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Wilaya
from .forms import *
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
from .models import PointOfSale
from .forms import PointOfSaleForm
from django.http import HttpResponse
import csv
from openpyxl import Workbook
from openpyxl import load_workbook
from django.contrib.auth.decorators import login_required


@login_required
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

@login_required
# Liste des prix
def price_list(request):
    # Récupérer tous les prix
    prices = ProductPrice.objects.all()

    # Initialiser le formulaire de filtrage
    filter_form = ProductPriceFilterForm(request.GET)

    # Appliquer les filtres si le formulaire est valide
    if filter_form.is_valid():
        product = filter_form.cleaned_data.get('product')
        point_of_sale = filter_form.cleaned_data.get('point_of_sale')
        price_min = filter_form.cleaned_data.get('price_min')
        price_max = filter_form.cleaned_data.get('price_max')
        date_from = filter_form.cleaned_data.get('date_from')
        date_to = filter_form.cleaned_data.get('date_to')

        if product:
            prices = prices.filter(product__name__icontains=product)  # Filtre par nom du produit
        if point_of_sale:
            prices = prices.filter(point_of_sale__name__icontains=point_of_sale)  # Filtre par nom du point de vente
        if price_min:
            prices = prices.filter(price__gte=price_min)  # Filtre par prix minimum
        if price_max:
            prices = prices.filter(price__lte=price_max)  # Filtre par prix maximum
        if date_from:
            prices = prices.filter(date_from__gte=date_from)  # Filtre par date de début
        if date_to:
            prices = prices.filter(date_to__lte=date_to)  # Filtre par date de fin

    return render(request, 'price_list.html', {
        'prices': prices,
        'filter_form': filter_form,
    })

# Créer un prix
def price_create(request):
    if request.method == 'POST':
        # Vérifie si le formulaire d'import CSV a été soumis
        if 'import_csv' in request.POST and 'csv_file' in request.FILES:
            csv_file = request.FILES['csv_file']
            
            # Lit le fichier CSV
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)

            # Importe chaque ligne dans la base de données
            for row in reader:
                product = Product.objects.get(name=row['Produit'])  # Récupère le Produit associé
                point_of_sale = PointOfSale.objects.get(name=row['Point de vente'])  # Récupère le Point de vente associé
                ProductPrice.objects.create(
                    product=product,
                    point_of_sale=point_of_sale,
                    price=row['Prix'],
                    date_from=row['Date de début'],
                    date_to=row['Date de fin'] if row['Date de fin'] else None
                )

            return redirect('price_list')  # Redirige vers la liste des Prix après l'import

        # Si le formulaire de création d'un Prix est soumis
        elif 'save_price' in request.POST:
            form = ProductPriceForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('price_list')

    else:
        form = ProductPriceForm()  # Affiche un formulaire vide pour la création manuelle

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

@login_required
# Liste des paniers
def basket_list(request):
    baskets = Basket.objects.all()
    return render(request, 'basket_list.html', {'baskets': baskets})

# Créer un panier
def basket_create(request):
    if request.method == 'POST':
        # Vérifie si le formulaire d'import Excel a été soumis
        if 'import_excel' in request.POST and 'excel_file' in request.FILES:
            excel_file = request.FILES['excel_file']
            
            # Charge le fichier Excel
            wb = load_workbook(excel_file)
            ws = wb.active

            # Parcourt les lignes du fichier Excel (en ignorant l'en-tête)
            for row in ws.iter_rows(min_row=2, values_only=True):  # min_row=2 pour ignorer l'en-tête
                Basket.objects.create(
                    name=row[0],  # Nom
                    description=row[1]  # Description
                )

            return redirect('basket_list')  # Redirige vers la liste des paniers après l'import

        # Si le formulaire de création d'un panier est soumis
        elif 'save_basket' in request.POST:
            form = BasketForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('basket_list')

    else:
        form = BasketForm()  # Affiche un formulaire vide pour la création manuelle

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

@login_required
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


@login_required
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


@login_required
# Liste des wilayas
def wilaya_list(request):
    # Récupérer toutes les wilayas
    wilayas = Wilaya.objects.all()

    # Initialiser le formulaire de filtrage
    filter_form = WilayaFilterForm(request.GET)

    # Appliquer les filtres si le formulaire est valide
    if filter_form.is_valid():
        code = filter_form.cleaned_data.get('code')
        name = filter_form.cleaned_data.get('name')

        if code:
            wilayas = wilayas.filter(code__icontains=code)  # Filtre par code (insensible à la casse)
        if name:
            wilayas = wilayas.filter(name__icontains=name)  # Filtre par nom (insensible à la casse)

    return render(request, 'wilaya_list.html', {
        'wilayas': wilayas,
        'filter_form': filter_form,
    })


# Créer une wilaya
def wilaya_create(request):
    if request.method == 'POST':
        # Vérifie si le formulaire d'import CSV a été soumis
        if 'import_csv' in request.POST and 'csv_file' in request.FILES:
            csv_file = request.FILES['csv_file']
            
            # Lit le fichier CSV
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)

            # Importe chaque ligne dans la base de données
            for row in reader:
                Wilaya.objects.create(
                    code=row['Code'],
                    name=row['Nom']
                )

            return redirect('wilaya_list')  # Redirige vers la liste des wilayas après l'import

        # Si le formulaire de création d'une wilaya est soumis
        elif 'save_wilaya' in request.POST:
            form = WilayaForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('wilaya_list')

    else:
        form = WilayaForm()  # Affiche un formulaire vide pour la création manuelle

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
        # Vérifie si le formulaire d'import CSV a été soumis
        if 'import_csv' in request.POST and 'csv_file' in request.FILES:
            csv_file = request.FILES['csv_file']
            
            # Lit le fichier CSV
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)

            # Importe chaque ligne dans la base de données
            for row in reader:
                wilaya = Wilaya.objects.get(name=row['Wilaya'])  # Récupère la Wilaya associée
                Moughataa.objects.create(
                    code=row['Code'],
                    name=row['Nom'],
                    wilaya=wilaya
                )

            return redirect('moughataa_list')  # Redirige vers la liste des Moughataas après l'import

        # Si le formulaire de création d'une Moughataa est soumis
        elif 'save_moughataa' in request.POST:
            form = MoughataaForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('moughataa_list')

    else:
        form = MoughataaForm()  # Affiche un formulaire vide pour la création manuelle

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



def export_wilaya_csv(request):
    # Crée une réponse HTTP avec le type de contenu CSV
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="wilayas.csv"'

    # Crée un écrivain CSV
    writer = csv.writer(response)
    
    # Écrit l'en-tête du CSV
    writer.writerow(['ID', 'Code', 'Nom'])

    # Récupère toutes les wilayas et écrit leurs données dans le CSV
    wilayas = Wilaya.objects.all()
    for wilaya in wilayas:
        writer.writerow([wilaya.id, wilaya.code, wilaya.name])

    return response

def import_wilaya_csv(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']
        
        # Lit le fichier CSV
        decoded_file = csv_file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)

        # Importe chaque ligne dans la base de données
        for row in reader:
            Wilaya.objects.create(
                code=row['Code'],
                name=row['Nom']
            )

        return redirect('wilaya_list')  # Redirige vers la liste des wilayas après l'import

    return render(request, 'import_wilaya.html')

def export_moughataa_csv(request):
    # Crée une réponse HTTP avec le type de contenu CSV
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="moughataas.csv"'

    # Crée un écrivain CSV
    writer = csv.writer(response)
    
    # Écrit l'en-tête du CSV
    writer.writerow(['ID', 'Code', 'Nom', 'Wilaya'])

    # Récupère toutes les moughataas et écrit leurs données dans le CSV
    moughataas = Moughataa.objects.select_related('wilaya').all()
    for moughataa in moughataas:
        writer.writerow([moughataa.id, moughataa.code, moughataa.name, moughataa.wilaya.name])

    return response

def export_price_csv(request):
    # Crée une réponse HTTP avec le type de contenu CSV
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="prices.csv"'

    # Crée un écrivain CSV
    writer = csv.writer(response)
    
    # Écrit l'en-tête du CSV
    writer.writerow(['ID', 'Produit', 'Point de vente', 'Prix', 'Date de début', 'Date de fin'])

    # Récupère tous les prix et écrit leurs données dans le CSV
    prices = ProductPrice.objects.select_related('product', 'point_of_sale').all()
    for price in prices:
        writer.writerow([
            price.id,
            price.product.name,
            price.point_of_sale.name,
            price.price,
            price.date_from,
            price.date_to
        ])

    return response

def export_basket_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="baskets.xlsx"'

    wb = Workbook()
    ws = wb.active
    ws.title = "Paniers"

    # En-têtes
    ws.append(['ID', 'Nom', 'Description'])

    # Données
    baskets = Basket.objects.all()
    for basket in baskets:
        ws.append([basket.id, basket.name, basket.description])

    wb.save(response)
    return response



    
#la tense 3n hun yalla tcontinie vih 4e lvogou !!

