from django.conf.urls import include, url
from . import views

urlpatterns = [
   url(r'esteban', views.GreetingsApp.as_view(), name="get_greeting"),
   url(r'home', views.home, name="homepage"),
   url(r'', views.login, name="loginpage"),


]
