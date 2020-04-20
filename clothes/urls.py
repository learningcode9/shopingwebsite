from django.urls import path
from clothes import views



urlpatterns = [
    path("",views.home,name='home'), 
    path("dresses/",views.dresses,name='dresses'),
    path("sarees/",views.sarees,name='sarees'),
    path("Lehangas/",views.lehangas,name='Lehangas'),
    path("checkout/",views.add_to_cart,name='checkout')
]

