from django.urls import path

from . import views

urlpatterns = [
    # category urls
    path('category/', views.CategoryView.as_view()),
    path('category/<int:id>/', views.CategoryDetailView.as_view()),
    # collections urls
    path('collection/', views.CollectionView.as_view()),
    path('collection/<int:id>/', views.CollectionDetailView.as_view()),
    # products urls
    path('product/', views.ProductView.as_view()),
    path('product/<int:id>/', views.ProductDetailView.as_view()),
    # add to cart
    path('addtocart/<int:id>/', views.AddToCartView.as_view()),

]