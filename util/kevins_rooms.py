from django.contrib.auth.models import User
from adventure.models import Player, Room


r_gardner = Room(title="Gardners Garden", description="""This garden has grown the most lavish
 fruits and vegetables on the planet, look around you for
 fruits and vegetables.""")

r_tomb = Room(title="The Kings Tomb", description="""You've found the long-lost Kings Tomb! 
Press C to loot the tomb.""")

r_princess_peach_castle = Room(title="Princess Peach castle", description="""You've arrived to Princess Peach Castle!
 See if she has anything for you.""")

r_bowsers_dungeon = Room(title="Bowsers Dungeon", description="""You're in Bowsers Dungeon,
 get what you can and get out of there!""")

r_toad_town = Room(title="Toad Town", description="""Toad town is iconic, for housing some of the worlds biggest superstars.
Look around and you might see Mario!""")

r_bonies_cabin = Room(title="Bonies Cabin", description="""Bonie welcomed you inside, for food.""")

r_goodnights_theatre = Room(title="Goodnights Theatre", description="""Shhhh!
 The show is about to start.""")

r_yoshis_yoga_palace = Room(title="Yoshis Yoga Palace", description="""Sit down, close your
 eyes and find your inter zen.""")

r_sarasaland = Room(title="Sarasaland", description="""Queen Daisy has been awaiting you're arrival,
 check what you can do for her.""")

r_bowsers_kingdom = Room(title="Bowsers Kingdom", description="""Watch youself, you might be standing on lava!""")

r_warios_woods = Room(title="Warios Woods", description="""Warios Woods has plenty of organic resources, pack up what you can and head to the market!""")

r_rosalinas_land = Room(title="Rosalinas Land", description="""You've found the long-lost land of Princess Rosalina! 
The Lumas have left everything! Where could they be?""")

r_koopalings_shack = Room(title="Kooplings Shack", description="""find a bed and get some rest.""")

r_lumas_village = Room(title="Lumas Village", description="""Lumas village is known for its amazing sky at night, and great tradesmen.
 See if anyone wants to trade anything.""")

r_toads_boat = Room(title="Toads Boat", description="""Toad said he'd take you to a special Island.
 Do you want to go?""")

r_toads_island = Room(title="Toads Island", description="""See what the people here have to offer.""")

r_marios_palace = Room(title="Marios Palace", description="""You've been selected to explore Marios palace.""")



r_gardner.save()
r_tomb.save()
r_princess_peach_castle.save()
r_bowsers_dungeon.save()
r_toad_town.save()
r_bonies_cabin.save()
r_goodnights_theatre.save()
r_yoshis_yoga_palace.save()
r_sarasaland.save()
r_bowsers_kingdom.save()
r_warios_woods.save()
r_rosalinas_land.save()
r_koopalings_shack.save()
r_lumas_village.save()
r_toads_boat.save()
r_toads_island.save()
r_marios_palace.save()