from django.contrib.auth.models import User
from adventure.models import Player, Room


allRooms = [x for x in Room.objects.all()]
roads = allRooms[:5]#4
desert = allRooms[5:24]#18
twisted = allRooms[24:43]#18
mushKing = allRooms[43:61]#17
borgHome = allRooms[61:]#20

# Connecting the rooms and the roads
import random

directions = [["n", "s"], ["s", "n"], ["e", "w"], ["w", "e"]]

rndnum = random.randint(1, 16)
rnddir = random.choice(directions)

shurima = desert[rndnum:] + desert[:rndnum]
places = twisted[rndnum:] + twisted[:rndnum]
marios_world = mushKing[rndnum:] + mushKing[:rndnum]
borg_hoard = borgHome[rndnum:] + borgHome[:rndnum]


# Link roads together
roads[0].connectRooms(roads[1], "s")# desert
roads[1].connectRooms(roads[0], "n")# shurima

roads[0].connectRooms(roads[2], "n")# twisted
roads[2].connectRooms(roads[0], "s")# places

roads[0].connectRooms(roads[3], "w")# mushKing
roads[3].connectRooms(roads[0], "e")# marios_world

roads[0].connectRooms(roads[4], "e")# borgHome
roads[4].connectRooms(roads[0], "w")# borg_hoard


# Link rooms together
roads[1].connectRooms(shurima[0], "n")
shurima[0].connectRooms(roads[1], "s")

roads[2].connectRooms(places[0], "s")
places[0].connectRooms(roads[2], "n")

roads[2].connectRooms(marios_world[0], "w")
marios_world[0].connectRooms(roads[2], "e")

roads[3].connectRooms(borg_hoard[0], "e")
borg_hoard[0].connectRooms(roads[3], "w")



c, i, temp = 1, 0, []
while i < len(shurima)/2:
  if c >= len(shurima):
    c = i + 1
  temp = rnddir
  shurima[i].connectRooms(shurima[c], temp[1])
  shurima[c].connectRooms(shurima[i], temp[0])
  c += 2
  i += 1


c, i, temp = 1, 0, []
while i < len(places)/2:
  if c >= len(places):
    c = i + 1
  temp = rnddir
  places[i].connectRooms(places[c], temp[1])
  places[c].connectRooms(places[i], temp[0])
  c += 2
  i += 1


c, i, temp = 1, 0, []
while i < len(marios_world)/2:
  if c >= len(marios_world):
    c = i + 1
  temp = rnddir
  marios_world[i].connectRooms(marios_world[c], temp[1])
  marios_world[c].connectRooms(marios_world[i], temp[0])
  c += 2
  i += 1


c, i, temp = 1, 0, []
while i < len(borg_hoard)/2:
  if c >= len(borg_hoard):
    c = i + 1
  temp = rnddir
  borg_hoard[i].connectRooms(borg_hoard[c], temp[1])
  borg_hoard[c].connectRooms(borg_hoard[i], temp[0])
  c += 2
  i += 1


players=Player.objects.all()
for p in players:
  p.currentRoom=roads[0].id
  p.save()

  