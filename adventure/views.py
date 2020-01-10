from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import *
from .serializers import *


@csrf_exempt
def allRooms(request):
    """
    List all rooms.
    """
    rooms = [{
      "title": x.title,
      "description": x.title,
      "players": x.playerNames(0)} for x in Room.objects.all()]
    return JsonResponse(rooms, safe=False)

@csrf_exempt
def singleRoom(request, pk):
    """
    Retrieve 1 room.
    """
    try:
        item = Room.objects.get(id=pk)
        room = {
          "title": item.title,
          "description": item.title,
          "players": item.playerNames(0)}
    except Room.DoesNotExist:
        return HttpResponse(status=404)
    return JsonResponse(room, safe=False)