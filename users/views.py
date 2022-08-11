from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer,RegisterSerializer, AuthTokenSerializer
from . models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from rest_framework.authtoken import views as auth_views
from rest_framework.compat import coreapi, coreschema
from rest_framework.schemas import ManualSchema



# Class based view to Get User Details using Token Authentication
class UserDetailAPI(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)

  def get(self,request,*args,**kwargs):
    user = User.objects.get(id=request.user.id)
    serializer = UserSerializer(user)
    return Response(serializer.data)

#Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer

class AuthToken(auth_views.ObtainAuthToken):
  serializer_class = AuthTokenSerializer
  if coreapi is not None and coreschema is not None:
      schema = ManualSchema(
          fields=[
              coreapi.Field(
                  name="email",
                  required=True,
                  location='form',
                  schema=coreschema.String(
                      title="Email",
                      description="Valid email for authentication",
                  ),
              ),
              coreapi.Field(
                  name="password",
                  required=True,
                  location='form',
                  schema=coreschema.String(
                      title="Password",
                      description="Valid password for authentication",
                  ),
              ),
          ],
          encoding="application/json",
      )