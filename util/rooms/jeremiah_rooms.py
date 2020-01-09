from django.contrib.auth.models import User
from adventure.models import Player, Room

r_adamantium = Room(title = "Adamantium Room",
                    description = """There seem to be claw like slashes all 
                    over the room!""")

r_web = Room(title = "Web Room",
             description = """There are sticky webs all over this room.""")

r_stark = Room(title = "Stark's Room",
               description = """There are vast amounts of electronics all over
                this room.""")

r_pitch_black = Room(title = "Pitch Black",
                     description = """Silence and darkness. You can't see
                      anything in this room.""")

r_science = Room(title = "Science Room",
                 description = """It looks as though a monster
                  tore out of this room.""")

r_skull = Room(title = "The Skull Room",
               description = """Guns and amo everywhere. There is a picture
                of a death's head skull on the wall.""")

r_cerebro = Room(title = "Cerebro",
                 description = """There is a weird helmet in the middle of 
                 this round room. Its like we are in a ball.""")

r_rock = Room(title = "The Rock",
              description = """Everywhere you look things are made of rock.""")

r_bullseye = Room(title = "The Bullseye Room",
                  description = """Hanging all around the room are targets 
                  that have been hit dead in the bullseye.""")

r_tourch = Room(title = "Tourch", description = """Everything is on fire.""")

r_ice = Room(title = "Ice", description = """Its so cold.""")

r_small = Room(title = "Small Room",
               description = """Everything in here is so tiny. 
               Like it was made for ants.""")

r_aquarium = Room(title = "Aquarium",
                  description = """All of the walls are fish tanks. There 
                  seems to be an entrance through the floor to the tank.""")

r_lightning = Room(title = "Lightning",
                   description = """This room seems to be charged with 
                   electricty. Don't touch the walls.""")

r_dead_pool = Room(title = "Deadpool's Room",
                   description = """There are little deadpool figurines 
                   everywhere. They all look to be dying though.""")

r_hawk = Room(title = "Hawk Room",
              description = """There is a perch in the corner of the room.""")

r_america = Room(title = "American Room",
                 description = """Captain America stuff is everywhere.""")

r_smash = Room(title = "Smash Room",
               description = """You can see several Hulk shirts ripped apart. 
               All the little Hulk figurines have been smashed into little 
               bitty peaces. """)

places = [r_adamantium, r_america, r_aquarium, r_bullseye, r_cerebro,
              r_dead_pool, r_hawk, r_ice, r_lightning, r_pitch_black, r_rock,
              r_science, r_skull, r_small, r_smash, r_stark, r_tourch, r_web]

for b in places:
    b.save()
