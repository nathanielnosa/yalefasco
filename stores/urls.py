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
    # users cart
    path('mycart/', views.MyCartView.as_view()),
    # manage cart
    path('managecart/<int:id>/', views.ManageCartView.as_view()),
    # checkout
    path('checkout/', views.CheckoutView.as_view()),
    # payment
    path('payment/<int:id>/', views.PaymentView.as_view(),name='payment'),
    # verify
    path('<str:ref>/', views.VerifyPaymentView.as_view()),
]