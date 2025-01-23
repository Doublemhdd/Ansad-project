from django.urls import path
from . import views
from django.contrib.auth import views as auth_views  # Import des vues d'authentification

urlpatterns = [
    # Page d'accueil
    path('home/', views.home, name='home'),

    # URLs pour l'authentification
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Moughataa
    path('moughataas/', views.moughataa_list, name='moughataa_list'),
    path('moughataas/create/', views.moughataa_create, name='moughataa_create'),
    path('moughataas/update/<int:pk>/', views.moughataa_update, name='moughataa_update'),
    path('moughataas/delete/<int:pk>/', views.moughataa_delete, name='moughataa_delete'),
    path('moughataa/export/', views.export_moughataa_csv, name='export_moughataa_csv'),

    # Wilayas
    path('wilayas/', views.wilaya_list, name='wilaya_list'),
    path('wilayas/create/', views.wilaya_create, name='wilaya_create'),
    path('wilayas/update/<int:pk>/', views.wilaya_update, name='wilaya_update'),
    path('wilayas/delete/<int:pk>/', views.wilaya_delete, name='wilaya_delete'),
    path('wilaya/export/', views.export_wilaya_csv, name='export_wilaya_csv'),
    path('wilaya/import/', views.import_wilaya_csv, name='import_wilaya_csv'),

    # Communes
    path('communes/', views.commune_list, name='commune_list'),
    path('communes/create/', views.commune_create, name='commune_create'),
    path('communes/update/<int:pk>/', views.commune_update, name='commune_update'),
    path('communes/delete/<int:pk>/', views.commune_delete, name='commune_delete'),

    # Produits
    path('products/', views.product_list, name='product_list'),
    path('products/create/', views.product_create, name='product_create'),
    path('products/update/<int:pk>/', views.product_update, name='product_update'),
    path('products/delete/<int:pk>/', views.product_delete, name='product_delete'),

    # Paniers
    path('baskets/', views.basket_list, name='basket_list'),
    path('baskets/create/', views.basket_create, name='basket_create'),
    path('baskets/update/<int:pk>/', views.basket_update, name='basket_update'),
    path('baskets/delete/<int:pk>/', views.basket_delete, name='basket_delete'),
    path('basket/export/', views.export_basket_excel, name='export_basket_excel'),

    # Prix
    path('prices/', views.price_list, name='price_list'),
    path('prices/create/', views.price_create, name='price_create'),
    path('prices/update/<int:pk>/', views.price_update, name='price_update'),
    path('prices/delete/<int:pk>/', views.price_delete, name='price_delete'),
    path('price/export/', views.export_price_csv, name='export_price_csv'),

    # Points de vente
    path('points-of-sale/', views.point_of_sale_list, name='point_of_sale_list'),
    path('points-of-sale/create/', views.point_of_sale_create, name='point_of_sale_create'),
    path('points-of-sale/update/<int:pk>/', views.point_of_sale_update, name='point_of_sale_update'),
    path('points-of-sale/delete/<int:pk>/', views.point_of_sale_delete, name='point_of_sale_delete'),
]