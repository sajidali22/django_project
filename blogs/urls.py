from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='blogs-home'),
    path('about/', views.about, name='blogs-about'),
]
