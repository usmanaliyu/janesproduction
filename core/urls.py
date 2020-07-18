from django.urls import path


from . import views
from .views import (
    ItemDetailView,
    CheckoutView,
    HomeView,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    PaymentView,
    AddCouponView,
    RequestRefundView,

    Search,
    CategoryView,
    AboutView,
    ContactView,
    UserView,
    PaystackView,
    paysuccess,
    ContactSuccess,
    terms,
    faq,
    privacy,
    payfail,
    ShopListView,
    SingleView,
    UserOrderView,
    UserAddressView,
    UserProfileView,

)

app_name = 'core'

urlpatterns = [
    path('', HomeView, name='home'),
    path('shop/', ShopListView.as_view(), name='shop'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView, name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
    path('search/', Search, name='search'),
    path('category/<slug>/', CategoryView, name='categoryview'),
    path('about/', AboutView, name='about'),
    path('contact/', ContactView, name='contact'),
    path('dashboard/', UserView, name='user'),
    path('dashboard/single/', SingleView, name='single'),
    path('dashboard/order/', UserOrderView, name='dashorder'),
    path('dashboard/address/', UserAddressView, name='address'),
    path('dashboard/profile/', UserProfileView, name='profile'),
    path('janepay/', PaystackView.as_view(), name='janepay'),
    path('paystack-success/', views.paysuccess, name='paystack-success'),
    path('paystack-failed/', views.payfail, name='paystack-failed'),
    path('contact-success/', views.ContactSuccess, name='contact-success'),
    path('terms-and-conditions/', views.terms, name='terms'),
    path('faq/', views.faq, name='faq'),
    path('privacy-policy/', views.privacy, name='privacy'),
    path('returns-and-exchange/', views.returns, name='returns'),
    path('shipping-info/', views.shippinginfo, name='shippinginfo'),
    path('signup/', views.SignUp.as_view(), name='signup'),


]
