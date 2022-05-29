from . import views
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static



urlpatterns=[
  path('', views.home, name='home'),
  path('search/', views.search, name='search'),
  re_path(r'^location/(?P<location_id>\d+)',views.location,name ='location'),
  re_path(r'^category/(?P<category_id>\d+)',views.category,name ='category'),
  re_path(r'^image/(?P<image_id>\d+)',views.image,name ='image'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    