from django.urls import path
from api_v1 import views

urlpatterns = [
    path('get_data/', views.get_data),
    path('add_data/', views.add_data),
]

