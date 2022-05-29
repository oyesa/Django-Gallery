from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static



urlpatterns=[
  path('', views.home, name='home'),
  path('search/', views.search, name='search'),
  path('location/', views.location, name='location'),
  path('category/', views.category, name='category')
]