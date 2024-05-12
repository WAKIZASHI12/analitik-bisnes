from django.urls import path
from . import views



urlpatterns = [
    path('processes/', views.view_processes, name='view_processes'),
    # Другие URL-маршруты вашего приложения
]