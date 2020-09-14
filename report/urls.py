from django.urls import path
from . import views

urlpatterns = [
    path('', views.print_users, name='index'),
    path('booking/', views.booking, name='booking'),
    path('inquiry/', views.inquiry, name='inquiry'),
    path('event/', views.event, name='event'),
]
