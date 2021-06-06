from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('products/',views.products, name="products"),
    path('customer/<str:pk>', views.customer, name="customer"),
    path('user/',views.userPage, name="user"),
    path('account/', views.accountSettings, name="account"),

    path('create_order/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>',views.deleteOrder,name="delete_order"),
   
    path('register/', views.registerPage, name="register"),
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logOutUser,name="logout"),


]
