from rest_framework import serializers
from api.models import Game
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    games = serializers.PrimaryKeyRelatedField(many=True, queryset=Game.objects.all(), allow_null=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'games']
    
class GameSerializer(serializers.ModelSerializer):
    # TODO : do not work
    #owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Game
        fields = ['id', 'owner', 'path', 'analyze_path']