from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.all_products),
    path('products/<int:product_id>/', views.product, name='product'),
    path('categories/', views.all_categories, name='category'),
    path('categories/<int:category_id>/', views.category, name="categore"),
    path('categories/<int:id>/products/', views.products_by_category)
]
