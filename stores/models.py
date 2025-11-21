from django.db import models
import uuid
import secrets

from users.models import Profile

# category
class Category(models.Model):
    # men fas, women fash, men access, women access
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='category', null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# collection 
class Collection(models.Model):
    # best seller, new arrival , accessories
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# products
SIZES = (
    ('M','M'),
    ('L','L'),
    ('XL','XL'),
    ('XXL','XXL')
)
COLORS = (
    ('black','black'),
    ('blue','blue'),
    ('pink','pink')
)
class Product(models.Model):
    title = models.CharField(max_length=255,unique=True)
    description = models.TextField()
    price = models.BigIntegerField()
    discount_price = models.BigIntegerField(null=True,blank=True)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    main = models.ImageField(upload_to='product')
    photo1 = models.ImageField(upload_to='product',null=True,blank=True)
    photo2 = models.ImageField(upload_to='product',null=True,blank=True)
    photo3 = models.ImageField(upload_to='product',null=True,blank=True)
    photo4 = models.ImageField(upload_to='product',null=True,blank=True)
    photo5 = models.ImageField(upload_to='product',null=True,blank=True)
    photo6 = models.ImageField(upload_to='product',null=True,blank=True)
    photo7 = models.ImageField(upload_to='product',null=True,blank=True)
    product_id = models.UUIDField(default=uuid.uuid4,unique=True)
    rating = models.IntegerField(default=0)
    review = models.TextField()
    in_stock = models.IntegerField()
    available = models.BooleanField(default=True)
    size = models.CharField(max_length=50,choices=SIZES)
    color = models.CharField(max_length=50,choices=COLORS)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        if not self.product_id:
            self.product_id = uuid.uuid4()
        super().save(*args,**kwargs)


# cart
class Cart(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True,blank=True)
    total = models.BigIntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Cart-{self.id} ::::> {self.total}'


# cart product
class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    subtotal = models.IntegerField()
    quantity = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Cart_id{self.cart.id} - quantity{self.quantity}'
    
# order
PAYMENT_METHOD = (
    ('paystack','paystack'),
    ('paypal','paypal'),
    ('transfer','transfer')
)
ORDER_STATUS = (
    ('completed','completed'),
    ('pending','pending'),
    ('failed','failed'),
    ('reverse','reverse')
)
class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    order_by = models.CharField(max_length=255)
    shipping_address = models.TextField()
    mobile = models.CharField(max_length=50)
    email = models.EmailField()
    amount = models.BigIntegerField()
    subtotal = models.BigIntegerField()
    order_status = models.CharField(max_length=255, choices=ORDER_STATUS, default='pending')
    payment_method = models.CharField(max_length=255, choices=PAYMENT_METHOD, default='paystack')
    payment_completed = models.BooleanField(default=False)
    ref  = models.CharField(max_length=255,unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Payment Completed-{self.payment_completed} - {self.order_status}'

    def save(self,*args,**kwargs):
        while not self.ref:
            ref = secrets.token_urlsafe(50)
            obj_with_sm_ref = Order.objects.filter(ref=ref)
            if not obj_with_sm_ref:
                self.ref = ref
        super().save(*args,**kwargs)
    
    # convert amount
    def amount_value(self)->int:
        return self.amount * 100

    # verify payment

