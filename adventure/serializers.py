from rest_framework import serializers

from .models import Player, Room


class RoomSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Room
    fields = ['id', 'title', 'description', 'playerNames']

class PlayerSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Player
    fields = ['id', 'user', 'currentRoom']