from .models import ShipmentCharge,Currency
from about_us.models import AboutUs
from cart.views import get_cart
from cart.models import CartItem

def ShipContext(request):
    charge = ShipmentCharge.objects.first()
    return {'charge':charge}

def CurrencyContext(request):
    currency = Currency.objects.first()
    return {'currency':currency}

def AboutUsContext(request):
    about_us = AboutUs.objects.first()
    return {'about_us':about_us}

def TotalCartItems(request):
    try:
        cart = get_cart(request)
        total_cartitem = CartItem.objects.filter(cart = cart,order_status = False).count()
    except:
        total_cartitem = 0
    return {'total_cartitem':total_cartitem} 