from django.urls import path
from .views import UserDetailAPI, RegisterUserAPIView, RequestAPI

urlpatterns = [
  path("get-details",UserDetailAPI.as_view()),
  path('register',RegisterUserAPIView.as_view()),
  path('get_result', RequestAPI.as_view())
]