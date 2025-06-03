from django.shortcuts import render,redirect
from .models import Cart,CartItem,Coupon,ConfirmOrder
from django.contrib.auth.decorators import login_required
from product.views import get_product,http
from django.utils.timezone import datetime
from django.contrib import messages
from common.models import ShipmentCharge
from .forms import OrderForm
from django.core.paginator import Paginator
# Create your views here.

def get_cart(request):
    try:
        return Cart.objects.get(user = request.user)
    except Cart.DoesNotExist:
        return None

def get_cartitem(id):
    try:
        return CartItem.objects.get(id = id)
    except CartItem.DoesNotExist:
        return None
    
def has_cart_item(cart,product):
    try:
        return CartItem.objects.get(product = product,cart = cart,order_status = False)
    except CartItem.DoesNotExist:
        return None
    
def get_total_price(cartitems):
    ship_charge = ShipmentCharge.objects.first()
    total_price = 0
    for cartitem in cartitems:
        total_price += cartitem.total_price
    max_total = total_price+ship_charge.outer_charge
    min_total = total_price+ship_charge.inner_charge
    return [
        total_price,
        min_total,
        max_total
        ]


@login_required(login_url = 'login')   
def MyCart(request):
    cart = get_cart(request)
    if not cart:
        return render(request,'404.html',{'message':'Cart not found'})
    cartitems = CartItem.objects.filter(cart = cart,order_status = False)
    prices = get_total_price(cartitems)
    total_price = prices[0]
    min_total = prices[1]
    max_total = prices[2]
    return render(request,'cart.html',{'cartitems':cartitems,'total_price':total_price,'min_total':min_total,'max_total':max_total})

@login_required(login_url = 'login')
def CheckOut(request):
    cart = get_cart(request)
    if not cart:
        return render(request,'404.html',{'message':'Cart not found'})
    total_price = 0
    cartitems = CartItem.objects.filter(cart = cart,order_status = False)
    prices = get_total_price(cartitems)
    total_price = prices[0]
    min_total = prices[1]
    max_total = prices[2]
    form = OrderForm()
    return render(request,'checkout.html',{'cartitems':cartitems,'total_price':total_price,'max_total':max_total,'min_total':min_total,'form':form})

@login_required(login_url = 'login')
def DeleteCartItem(request,id):
    cartitem = get_cartitem(id)
    cart = get_cart(request)
    if not cart:
        return render(request,'404.html',{'message':'Cart not found'})
    if not cartitem:
        return render(request,'404.html',{'message':'Item not found'})
    if cartitem.cart == cart:
        cartitem.delete()
    else:
        messages.warning(request,'You can\'t delete this')
    return redirect('mycart')

@login_required(login_url = 'login')
def IncreaseQty(request,id):
    cartitem = get_cartitem(id)
    cart = get_cart(request)
    if not cart:
        return render(request,'404.html',{'message':'Cart not found'})
    if not cartitem:
        return render(request,'404.html',{'message':'Item not found'})
    if cartitem.cart == cart:
        cartitem.qty += 1
        cartitem.product.stock -= 1
        cartitem.save()
        cartitem.product.save()
    else:
        messages.warning(request,'OOPS!')
    return redirect('mycart')

@login_required(login_url = 'login')
def DecreaseQty(request,id):
    cartitem = get_cartitem(id)
    cart = get_cart(request)
    if not cart:
        return render(request,'404.html',{'message':'Cart not found'})
    if not cartitem:
        return render(request,'404.html',{'message':'Item not found'})
    if cartitem.cart == cart:
        cartitem.qty -= 1
        cartitem.product.stock += 1
        cartitem.save()
        cartitem.product.save()
    else:
        messages.warning(request,'OOPS!')
    return redirect('mycart')

@login_required(login_url = 'login')
def AddProduct(request,id):
    product = get_product(id)
    cart = get_cart(request)
    cartitem = has_cart_item(cart,product)
    qty = int(request.POST.get('qty',1))
    if cart:
        if product:
            if cartitem:
                cartitem.qty += qty
                cartitem.save()
            else:
                new_item = CartItem(cart = cart,product = product)
                new_item.save()
            product.stock -= qty
            product.save()
            return redirect('all-product')
        else:
            return render(request,'404.html',{'message':'Product not available'})
    else:
        return render(request,'404.html',{'message':'Cart not found'})
    

@login_required(login_url = 'login')
def ConfirmUserOrder(request):
    cart = get_cart(request)
    if not cart:
        return render(request, '404.html', {'message': 'Cart not found'})
    
    cartitems = CartItem.objects.filter(cart=cart, order_status=False)
    if not cartitems.exists():
        return render(request, '404.html', {'message': 'Cart is empty'})
    
    prices = get_total_price(cartitems)
    total_price = prices[0]

    if request.method == 'POST':
        form = OrderForm(data=request.POST)
        code = request.POST.get('code',False)
        if code:
            coupon = Coupon.objects.get(code=code)
        else:
            coupon = False
            
        if form.is_valid():
            order = form.save(commit=False)
            order.cart = cart

            if coupon and coupon.is_active == True:
                order.coupon = coupon
                discount_price = (total_price * coupon.discount) / 100
                order.discount_price = total_price - discount_price
            
            order.total_price = total_price
            order.save()
            order.products.set(cartitems)
            order.save()

            messages.success(request, 'Order placed successfully!')
            return redirect('my-orders')
        else:
            messages.error(request, 'An error occurred while submitting the form')

    return render(request, '404.html', {'message': 'Invalid request method'})

@login_required(login_url = 'login')
def MyOrders(request):
    cart = get_cart(request)
    orders = ConfirmOrder.objects.filter(cart = cart)
    paginator = Paginator(orders,10)
    page_num = request.GET.get('page')
    order_objs = paginator.get_page(page_num)
    return render(request,'my-order.html',{'orders':order_objs})






