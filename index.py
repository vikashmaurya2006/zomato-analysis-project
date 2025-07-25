# landing/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
# mysite/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('landing.urls')),
    path('admin/', admin.site.urls),
]
