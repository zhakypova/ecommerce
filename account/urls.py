from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from . import views



urlpatterns = [
    path('register/sender/', views.SenderCreateAPIView.as_view()),
    path('register/buyer/', views.BuyerCreateAPIView.as_view()),
    path('token/', obtain_auth_token),

]
