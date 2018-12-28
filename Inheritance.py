class Hero:
	def __init__(self, name, health):
		self.name 		= name
		self.health 	= health

class HeroIntelegent(Hero):
	pass
		
class HeroStreang(Hero):
	pass

snipper = Hero("mas", 100)

print(snipper.name)

intel = HeroIntelegent("mama", 90)
print(intel.name)
superbanget = HeroStreang("super", 120)
print(superbanget.name)
		