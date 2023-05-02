
from django.urls import path
from . import views

urlpatterns = [
    path("login",views.LoginView.as_view()),
    path("register",views.RegisterAPI.as_view()),
    path("logout",views.LogoutView.as_view()),
    path("product",views.ProductAPI.as_view()),
    path("product/<int:id>",views.ProductAPI.as_view()),
    path("product/all",views.productAPIView.as_view())

]