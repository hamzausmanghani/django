from .views import RegisterAPI, LoginAPI, GetUserDetails
from knox import views as knox_views
from django.urls import path


urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/get_users/', GetUserDetails.as_view(), name="get_users")
]