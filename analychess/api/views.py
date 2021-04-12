from .serializers import GameSerializer, UserSerializer
from .models import Game, MyUser
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsOwnerOrReadOnly, IsMeOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request):
    return Response({
        'users': reverse('user-list', request=request),
        'games': reverse('game-list', request=request)
    })

class UserList(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer
    
    
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsMeOrReadOnly]
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer

class GameList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Game.objects.all()
    serializer_class = GameSerializer
