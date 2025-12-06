from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path

from .views import *

urlpatterns = [
    path("profile/", ProfileView.as_view(), name="profile"),
    path("change-password/", ChangePasswordView.as_view(), name="change_password"),
    path("login/", TokenObtainPairView.as_view(), name='login'),
    path("refresh/", TokenRefreshView.as_view(), name='refresh'),
]