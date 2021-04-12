from rest_framework import serializers
from .models import Game, MyUser
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    games = serializers.PrimaryKeyRelatedField(many=True, queryset=Game.objects.all(), allow_null=True)

    class Meta:
        model = MyUser
        fields = ['id', 'username', 'password', 'games', 'email']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSerializer, self).create(validated_data)

    def update(self,instance, validated_data):
        instance.username =validated_data.get('username', instance.username)
        instance.email =validated_data.get('email', instance.email)
        instance.games.set(validated_data.get('games', instance.games))
        instance.password = make_password(validated_data.get('password'))
        instance.save()
        return instance

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret.pop("password")
        return ret

        
    
class GameSerializer(serializers.ModelSerializer):
    # TODO : do not work
    #owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Game
        fields = ['id', 'owner', 'path', 'analyze_path']