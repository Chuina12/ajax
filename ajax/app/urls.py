from django.urls import path 
from . import views 

urlpatterns = [
    path('appCreateView', views.appCreateView.as_view(), name='appCreateView'),
]
