from django.urls import path
from .views import admin_fard_salah

urlpatterns = [
    path('',admin_fard_salah,name='adminfardsalah'),
]