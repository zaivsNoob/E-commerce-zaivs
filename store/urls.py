from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.registerView,name='register'),
   path('',views.storeView,name='store'),
   path('cart/',views.cartView,name="cart"),
   path('checkout/',views.checkoutView,name='checkout'),
   path('update_item/',views.updateItem,name='update-item'),
    path('login/',views.loginUser,name='login'),
       path('logout/',views.logoutUser,name='logout')
]
