
from django.urls import path
from .views import UserDetailAPI,RegisterUserAPIView, AuthToken, FindUser
urlpatterns = [
  path("get-details",UserDetailAPI.as_view()),
  path('register',RegisterUserAPIView.as_view()),
  path('get-auth-token', AuthToken.as_view()),
  path('find', FindUser)
]