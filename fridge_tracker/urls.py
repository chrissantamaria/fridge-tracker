from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('', views.index),
    path('accounts/', include('user_auth.urls')),
    path('admin/', admin.site.urls),
]
