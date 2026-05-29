from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index , name='index'),
    path('class11/', views.Class11 , name='class11'),
    path('class12/', views.Class12 , name='class12'),
    path('bcom/', views.bcom , name='bcom'),
    path('1st/', views.bcom_01 , name='1st'),
    path('2nd/', views.bcom_02 , name='2nd'),
    path('3rd/', views.bcom_03, name='3rd'),
    path('about/', views.about , name='about'),
    path('result/', views.result , name='result'),
    path('contact/' , views.contact_view , name='contact'),
    path('thank-you/', views.thankyou_view, name='thankyou'),
    path('process_contact/', views.process_contact_form, name='process_contact'),
]