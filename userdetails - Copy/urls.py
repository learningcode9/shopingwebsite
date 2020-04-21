from django.urls import path
from userdetails import views

urlpatterns = [
   
    path("Register/",views.Register,name="Register"),
    path("login/",views.login,name="login"),
    path("logout/", views.logout,name='logout'),
    path('activate/<uid64>/<token>',views.ActivateAccount,name='Activate')
   
]
