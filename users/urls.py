from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.userlogin.as_view()),
    path('logout/',views.userlogout.as_view()),
    path('shop/add/',views.shoplist.as_view()),
    path('shop/list/',views.shoplist.as_view()),
    path('shop/visit/',views.shopvisit.as_view()),
]