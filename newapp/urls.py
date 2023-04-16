from newapp import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('index', views.index, name='index'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('signup',views.signup,name='signup'),
    path('transportationlink',views.transportationlink,name='transportationlink'),
    path('transportation',views.transportation, name='transportation'),
    path('donate',views.donate,name='donate')
    
]