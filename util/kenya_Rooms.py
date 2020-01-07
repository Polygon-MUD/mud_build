#from django.contrib.auth.models import User
from adventure.models import Player, Room

#creating rooms and their descriptions 
r_suarward_dining = Room(title = "Suarward Dining", description = "Large, square dining room has mismatched wooden furniture.  The seating is cushioned.  The floor is stone. Overall has a quaint atmosphere.")

r_talltail_chambers = Room(title = "TallTail Chambers", description = "Small, rectangular bedroom with wooden funiture. Among the first things one notices walking in is muddy footprints on the floor.")

r_starStrike_sanctuary = Room(title = 'Starstrike Sanctuary', description = " This cramped, rectangular office has mismatched wooden, metal, and glass furniture, Upon entering one notices light from the heavens")

r_grandwing_saloon = Room(title = "Grandwing Saloon", description = "Cramped, square, dim lit saloon. Broken glass covers the floor. There is a thick haze of smoke upon entering. Among the first things one notices walking in are a conspicuous stain on the floor")

r_outcast_den = Room(title = "Outcast Den", description = "Large, L-shaped bathroom screams death. Leave Quickly!")

r_starfall_hideout = Room(title = "Starfall Hideout", description = "Light is provided by wall lamps and a ceiling light. Among the first things one notices walking in are glitter footprints on the floor and a collection of action figures.")

r_lightstorm_harbor = Room(title = "Lightstorm Harbor", description = "Among the first things one notices walking in is photographs on the wall. Long ago this was a sailors palace ")

r_feather_nest = Room(title = "Feather Nest", description= "A large, square bedroom. The floor is layered with shedded feathers. The first thing one notices upon entering is a broken clock on the wall")

r_coldwar_hideaway = Room(title = "Coldwar Hideaway", description= "The room is done in colors that remind you of Halloween and overall has a rustic look to it.  Among the first things one notices walking in are a crumpled paper")

r_shadow_burrow = Room(title = "Shadow Burrow", description= "Cold, and cluttered with spell books. Upon entering one feels a draft come from the window that chills the soul")

r_miracle_dungeon = Room(title = "Miracle Dungeon", description= "This large kitchen is magical. Powered by one's own imagination")

r_skullblade_cave = Room(title = "skullblade_cave", description= "An average-sized cave, dark and mysterious. Sounds of flowing water come from deep within. Among entering bats fly out from everywhere.")

r_thorn_nest = Room(title = "Thorn Nest", description= "Cramped office with matching wooden furniture. The room is done is such way it reminds one of a thorny nest")

r_archkeep_sanctuary = Room(title = "Archkeep Sanctuary", description= "This spacious, bathroom is done in bold colors and overall has a quaint atmosphere.  Among the first things one notices walking in are a collection of knickknacks and many cosmetics strewn on the counter.")

r_skyspell_haven = Room(title = "Skyspell Haven", description= "Vintage theme in murky colors and overall has a retro look to it.  Among the first things one notices walking in is a barn star on the wall.")

r_flower_retreat = Room(title = "Flower Retreat", description= "A mystical garden, that is home to many fairies, but beware the dragons below")

r_blitz_cover = Room(title = "Blitz Cover", description= "Underground, yet well lit. Blitz Cover is a reminder of safety in these parts")

r_mystery_lair = Room(title = "Mystery Lair", description= "The room of deja vu, beware!")


#saving rooms

places = [r_suarward_dining,
r_talltail_chambers,
r_starStrike_sanctuary,
r_grandwing_saloon,
r_outcast_den,
r_starfall_hideout,
r_lightstorm_harbor,
r_feather_nest,
r_coldwar_hideaway,
r_shadow_burrow,
r_miracle_dungeon,
r_skullblade_cave,
r_thorn_nest,
r_archkeep_sanctuary,
r_skyspell_haven,
r_flower_retreat,
r_blitz_cover,
r_mystery_lair]

for x in places: x.save()
