from django.urls import reverse
from rest_framework import serializers,status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *

from django.shortcuts import get_object_or_404
from django.db import transaction
from django.conf import settings

import requests

# :::: CATEGORY CRUD :::: #
# :::: CATEGORY CRUD :::: #
class CategoryView(APIView):
    # create category
    def post(self,request):
        try:
            serializers = CategorySerializer(data=request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data, status=status.HTTP_201_CREATED)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # get all categories
    def get(self, request):
        try:
            categories = Category.objects.all()
            serializers = CategorySerializer(categories, many=True)
            return Response(serializers.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CategoryDetailView(APIView):
    # get single category
    def get(self,request,id):
        try:
            category = get_object_or_404(Category, id=id)
            serializers = CategorySerializer(category)
            return Response(serializers.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # update category
    def put(self,request,id):
        try:
            category = get_object_or_404(Category, id=id)
            serializers = CategorySerializer(category, data=request.data, partial=True)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data, status=status.HTTP_200_OK)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # delete category
    def delete(self,request,id):
        try:
            category = get_object_or_404(Category, id=id)
            category.delete()
            return Response({"Message": "Category deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# :::: END OF  CATEGORY CRUD :::: #
# :::: END OF  CATEGORY CRUD :::: #

# :::: COLLECTION CRUD :::: #
# :::: COLLECTION CRUD :::: #
class CollectionView(APIView):
    # create collection
    def post(self,request):
        try:
            serializers = CollectionSerializer(data=request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data, status=status.HTTP_201_CREATED)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # get all collections
    def get(self, request):
        try:
            collections = Collection.objects.all()
            serializers = CollectionSerializer(collections, many=True)
            return Response(serializers.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CollectionDetailView(APIView):
    # get single collection
    def get(self,request,id):
        try:
            collection = get_object_or_404(Collection, id=id)
            serializers = CollectionSerializer(collection)
            return Response(serializers.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # update collection
    def put(self,request,id):
        try:
            collection = get_object_or_404(Collection, id=id)
            serializers = CollectionSerializer(collection, data=request.data, partial=True)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data, status=status.HTTP_200_OK)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # delete collection
    def delete(self,request,id):
        try:
            collection = get_object_or_404(Collection, id=id)
            collection.delete()
            return Response({"Message": "Collection deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# :::: END OF  COLLECTION CRUD :::: #
# :::: END OF  COLLECTION CRUD :::: #

# :::: PRODUCT CRUD :::: #
# :::: PRODUCT CRUD :::: #
class ProductView(APIView):
    # create product
    def post(self,request):
        try:
            serializers = ProductSerializer(data=request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data, status=status.HTTP_201_CREATED)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # get all products
    def get(self, request):
        try:
            products = Product.objects.all()
            serializers = ProductSerializer(products, many=True)
            return Response(serializers.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ProductDetailView(APIView):
    # get single product
    def get(self,request,id):
        try:
            product = get_object_or_404(Product, id=id)
            serializers = ProductSerializer(product)
            return Response(serializers.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # update product
    def put(self,request,id):
        try:
            product = get_object_or_404(Product, id=id)
            serializers = ProductSerializer(product, data=request.data, partial=True)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data, status=status.HTTP_200_OK)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # delete product
    def delete(self,request,id):
        try:
            product = get_object_or_404(Product, id=id)
            product.delete()
            return Response({"Message": "Product deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# :::: END OF  PRODUCT CRUD :::: #
# :::: END OF  PRODUCT CRUD :::: #

# :::: ADD TO CART :::: #
# :::: ADD TO CART :::: #

class AddToCartView(APIView):
    def post(self, request,id):
        try:
            # get the product
            product = get_object_or_404(Product, id=id)
            # get a cart
            cart_id = request.session.get("cart_id", None)
            # checking if price or discount price
            price = product.discount_price if product.discount_price else product.price

            while transaction.atomic:
                if cart_id:
                    # get the cart
                    cart = Cart.objects.filter(id=cart_id).first()
                    if cart is None:
                        cart = Cart.objects.create(total=0)
                        request.session['cart_id'] = cart.id
                    
                    # check if the product is already in the cart
                    this_product_in_cart = cart.cartproduct_set.filter(product=product)
                    
                    if this_product_in_cart.exists():
                        cartproduct = this_product_in_cart.last()
                        cartproduct.quantity += 1
                        cartproduct.subtotal += price
                        cartproduct.save()
                        cart.total += price
                        cart.save()
                        return Response({"Message": "Product quantity updated in cart successfully"}, status=status.HTTP_200_OK)
                    else:
                        cartproduct = CartProduct.objects.create(cart=cart,product=product,subtotal=price,quantity=1)
                        cartproduct.save()
                        cart.total += price
                        cart.save()
                        return Response({"Message": "Product added to cart successfully"}, status=status.HTTP_201_CREATED)
                else:
                    cart = Cart.objects.create(total=0)
                    request.session['cart_id'] = cart.id
                    cartproduct = CartProduct.objects.create(cart=cart,product=product,subtotal=price,quantity=1)
                    cartproduct.save()
                    cart.total += price
                    cart.save()
                    return Response({"Message": "Product added to cart successfully"}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# :::: END OF  ADD TO CART :::: #
# :::: END OF  ADD TO CART :::: #


# :::: MY CART :::: #
# :::: MY CART :::: #
class MyCartView(APIView):
    def get(self,request):
        try:
            cart_id = request.session.get("cart_id",None)
            if cart_id:
                cart = get_object_or_404(Cart, id=cart_id)
                # # assign cart to a user
                if request.user.is_authenticated and hasattr(request.user, 'profile'):
                    cart.profile = request.user.profile
                    cart.save()
                return Response({"Message": f"{cart.profile} owns this cart"},status=status.HTTP_200_OK)
            
            return Response({"Message": f"This cart is not found"},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# :::: END OF  MY CART :::: #
# :::: END OF  MY CART :::: #


# :::: MANAGE CART :::: #
# :::: MANAGE CART :::: #
class ManageCartView(APIView):
    def post(self,request,id):
        action = request.data.get("action",None)
        try:
            cart_obj = get_object_or_404(CartProduct, id=id)
            cart = cart_obj.cart
            price = cart_obj.product.discount_price if cart_obj.product.discount_price else cart_obj.product.price

            if action == "inc":
                cart_obj.quantity += 1
                cart_obj.subtotal += price
                cart_obj.save()
                cart.total+=price
                cart.save()
                return Response({"Message": "Cart Product increase successfully"}, status=status.HTTP_200_OK)
            if action == "dec":
                cart_obj.quantity -= 1
                cart_obj.subtotal -= price
                cart_obj.save()
                cart.total-=price
                cart.save()
                if cart_obj.quantity <=0:
                    cart_obj.delete()                
                return Response({"Message": "Cart Product decrease successfully"}, status=status.HTTP_200_OK)
            if action == "rmv":
                cart.total -= price
                cart.save()
                cart_obj.delete()
                return Response({"Message": "Cart Product removed successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# :::: END OF  MANAGE CART :::: #
# :::: END OF  MANAGE CART :::: #



# :::: CHECKOUT :::: #
# :::: CHECKOUT :::: #
class CheckoutView(APIView):
    def post(self,request):
        try:
            cart_id = request.session.get("cart_id",None)
            if not cart_id:
                return Response({"Message": "No cart found"}, status=status.HTTP_400_BAD_REQUEST)
            cart = get_object_or_404(Cart, id=cart_id)
            serializers = CheckoutSerializer(data=request.data)
            if serializers.is_valid():
                order = serializers.save(
                    cart=cart,
                    amount=cart.total,
                    subtotal=cart.total,
                    order_status = 'pending'
                )
                del request.session['cart_id']
                if order.payment_method == 'paystack':
                    # integrate paystack payment gateway here
                    payment_url = reverse("payment",args=[order.id])
                    return Response({"payment_url": payment_url}, status=status.HTTP_201_CREATED)
                return Response({"Message": "Order placed successfully", "order_id": order.id}, status=status.HTTP_201_CREATED)
            
                # elif order.payment_method == 'paypal':
                #     # integrate paypal payment gateway here
                #     pass
                # elif order.payment_method == 'transfer':
                #     # provide bank transfer details here
                #     pass
            return Response({"Message": "Payment Cant be verified"}, status=status.HTTP_201_CREATED)
                
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# :::: END OF  CHECKOUT :::: #
# :::: END OF  CHECKOUT :::: #


# :::: CHECKOUT :::: #
# :::: CHECKOUT :::: #
class PaymentView(APIView):
    def get(self,request,id):
        try:
            order = get_object_or_404(Order, id=id)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        url = f"https://api.paystack.co/transaction/initialize"
        headers ={"Authorization": f"Bearer {settings.PAYSTACK_SECRETE_KEY}"}
        data = {
            "email": order.email,
            "amount": order.amount * 100,
            "reference": order.ref,
        }
        response = requests.post(url,headers=headers,data=data)
        response_data= response.json()
        if response_data['status']:
            paystack_url = response_data['data']
            return Response(
                {
                    'order':order.id,
                    'total':order.amount,
                    'paystack_public_key':settings.PAYSTACK_PUBLIC_KEY,
                    'paystack_url': paystack_url
                }
            )
        else:
            return Response({"Message": "Payment initialization failed"}, status=status.HTTP_400_BAD_REQUEST)

# :::: END OF  CHECKOUT :::: #
# :::: END OF  CHECKOUT :::: #

# :::: VERIFY PAYMENT :::: #
# :::: VERIFY PAYMENT :::: #
class VerifyPaymentView(APIView):
    def get(self,request,ref):
        try:
            order = get_object_or_404(Order, ref=ref)
            url = f"https://api.paystack.co/transaction/verify/{ref}"
            headers ={
                "Authorization": f"Bearer {settings.PAYSTACK_SECRETE_KEY}",
                "Content-Type": "application/json",
            }
            response = requests.get(url, headers=headers)
            response_data = response.json()

            if response_data['status']:
                if response_data['data']['status'] == 'success':
                    order.payment_completed = True
                    order.order_status = 'completed'
                    order.save()
                    return Response({"Message": "Payment verified successfully"}, status=status.HTTP_200_OK)
                else:
                    order.payment_completed = False
                    order.order_status = 'failed'
                    order.save()
                    return Response({"Message": "Payment verification failed"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"Message": "Payment verification failed"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# :::: END OF  VERIFY PAYMENT :::: #
# :::: END OF  VERIFY PAYMENT :::: #
