from django.contrib.auth.models import User
from adventure.models import Player, Room


r_borg = Room(title="The Borg", description="""Prepare to be assimilated! Resistance is futile!""")

r_enterprise = Room(title="The Enterprise", description="""Space: the final frontier. Boldy go!""")

r_vulcan = Room(title="Planet Vulcan", description="""Live long and prosper.
 Just don't get emotional about it.""")

r_replicator = Room(title="The Replicator Room", description="""Order what you like.
 Picard recommneds: Tea, Earl Grey, hot!""")

r_alpha_quadrant = Room(title="Alpha quadrant", description="""Ready to see the neighborhood?
 Make it so!""")

r_transporter = Room(title="The Transporter Room", description="""If things get freaky down there,
 just call out: Beam me up, Scotty! When you are ready to go down just call out 'Engage!'""")

r_stranded = Room(title="Stranded on Unknown Planet", description="""Did I tell you the one about Darmok
 and Jalad at Tanagra?""")

r_holodeck = Room(title="The Holodeck", description="""Think of your wildest fantasy,
 and ypu're there. Try not to run into the walls. It can be a rude awakening.""")

r_tribble = Room(title="The Tribble Room", description="""The Trouble with Tribbles?
 Those cute little furry things? Why, they're no tribble a'tal.""")

r_romulan = Room(title="Romulan Warbird", description="""Get ready for battle!
 Death to the Cardassians!""")

r_shore_leave = Room(title="Shore Leave", description="""If you see Alice chasing a White Rabbit,
 tell her he went for a cup of tea.""")

r_earth = Room(title="Planet Earth", description="""Earth inhabitants: Ugly bags of mostly water.""")

r_klingon = Room(title="Klingon Home Planet", description="""Get ready for some Gok.
 Best when the worms are alive and wriggling. Wash it down with a warm glass of Blood Wine.""")

r_jefferies_tube = Room(title="Jefferies Tube", description="""Just keep your head down and crawl low.
 Don't touch that pipe. It might be scaldingly hot.
  And if you touch the high power line, don't worry--no pain with instant death.""")

r_delta_quadrant = Room(title="Delta Quadrant", description="""Thought you were going on a short test run?
 No problem. Just forty years back to the Alpha Quadrant. Talk about a long distance Voyager.""")

r_pon_farr = Room(title="Pon Farr", description="""Thought you could just forget about it
 and it would go away? No way. Time to pair up my mate. May as well have some wild fun.""")

r_neutral_zone = Room(title="The Neutral Zone", description="""Get out as quickly as you can.
 Breaking the treaty of the Neutral Zone is highly offensive.
  Watch out for that Romulan War bird. It's gunning for ya""")

r_bajoran_wormhole = Room(title="Bajoran Wormhole", description="""Thought the war on Bajora
 with the Cardassians was bad? Well, enjoy getting sucked into this Bajoran Wormhole.
  Maybe you will luck out and get to the other side and only have to face the Dominion.""")

r_baryon_sweep = Room(title="Baryon Sweep", description="""Such unfortunate timing my friend.
 You have managed to beam aboard a vessal undergoing a Baryon Sweep.
  Yes, any organic living matter will be neutralized when the Baryon Sweep gets to its position
   onboard the craft. Sure hope you are not organic.""")

r_cardassia_prime = Room(title="Cardassia Prime", description="""Lucky you.
 Very Festive times now on Cardassia Prime. Everyone is celebrating making war on Bajor.
  You are Bjoran you say? Uh oh!""")

borg_hoard = [r_borg, r_enterprise, r_vulcan, r_replicator, r_alpha_quadrant, r_transporter, r_stranded, r_holodeck, r_tribble, r_romulan, r_shore_leave, r_earth, r_klingon, r_jefferies_tube, r_delta_quadrant, r_pon_farr, r_neutral_zone, r_bajoran_wormhole, r_baryon_sweep, r_cardassia_prime ]

for b in borg_hoard:
  b.save() 