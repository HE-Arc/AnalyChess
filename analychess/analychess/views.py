from api.serializers import GameSerializer, UserSerializer
from api.models import Game
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions
from api.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status

@api_view(['GET'])
def logout(request):
    print(request.user.auth_token)
    print(dir(request.user.auth_token.delete()))
    request.user.auth_token.delete()    
    return Response("Logout succeed !", status=status.HTTP_200_OK)