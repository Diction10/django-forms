from django.urls import path

from . import views

# define url patterns for the app form1

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register')
]