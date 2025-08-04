from django.contrib import admin
from django.urls import path
from services import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('category/<int:id>/', views.category_services, name='category_services'),
]
