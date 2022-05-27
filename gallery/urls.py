from . import views
from django.conf import path
from django.conf import settings



urlpatterns=[
  path('', views.home, name='home'),
]