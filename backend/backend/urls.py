
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('financas.urls')),
    path('users/', include('Users.urls')),
]
