from .views import MyCart,CheckOut,IncreaseQty,DecreaseQty,DeleteCartItem,AddProduct,ConfirmUserOrder,MyOrders
from django.urls import path

urlpatterns = [
    path('add-product/<str:id>/',AddProduct,name = 'add-product'),
    path('mycart/',MyCart,name = 'mycart'),
    path('checkout/',CheckOut,name = 'checkout'),
    path('delete-cart-item/<str:id>/',DeleteCartItem,name = 'delete-cart-item'),
    path('increase-qty/<str:id>/',IncreaseQty,name = 'increase-qty'),
    path('decrease-qty/<str:id>/',DecreaseQty,name = 'decrease-qty'),
    path('confirm-order/',ConfirmUserOrder,name = 'confirm-order'),
    path('my-orders/',MyOrders,name = 'my-orders'),

]
