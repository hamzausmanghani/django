from django.urls import path
from itemsApp import views

urlpatterns = [
    path('get_data/', views.get_data),
    path('add_data/', views.add_data),
]

