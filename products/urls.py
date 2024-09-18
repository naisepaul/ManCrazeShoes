from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product,
         name='delete_product'),  
    path('<str:pk>/wishlist/', views.my_wishlist, name='my-wishlist'),
    path('wishlist_add/<str:pk>/',
         views.wishlist_add, name='wishlist-add'),
]
