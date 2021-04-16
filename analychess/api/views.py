from .serializers import GameSerializer, UserSerializer, AnalysisSerializer
from .models import Game, MyUser
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsOwnerOrReadOnly, IsMeOrReadOnly
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .parser.parser import parse
from django.http import JsonResponse
from rest_framework import status
import jwt
import datetime
from time import sleep
from django.conf import settings



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
    serializer_class = GameSerializer

    def get_queryset(self):
        user = self.request.user
        return Game.objects.filter(owner=user)

class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def delete(self, request, *args, **kwargs):
        game = self.get_object()
        # If last owner : delete the game
        if(len(game.owner.values()) == 1):
            return self.destroy(request, *args, **kwargs)
        # Else remove the current user from the game
        else:
            game.owner.remove(request.user)
            print(game.owner.all())
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def upload_pgn(request):
    pgn = parse(request.data['pgn'])
    return JsonResponse(AnalysisSerializer().serialize(pgn), safe=False)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def share(request):
    encoded_jwt = jwt.encode({"gameId": request.data['id'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=60*60)}, settings.SECRET_KEY, algorithm="HS256")
    return JsonResponse({"token": encoded_jwt})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def join(request):
    try:
        # decode the token
        game_id = jwt.decode(
            request.query_params["token"], settings.SECRET_KEY, algorithms=["HS256"]
        )
        
    except:
        return JsonResponse({"code": 400, "message": "invalid token"})

    Game.objects.filter(id=game_id["gameId"]).get().owner.add(request.user.id)


    return JsonResponse({"code": 200})
    

