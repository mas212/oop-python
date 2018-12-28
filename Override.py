class Hero:
	def __init__(self, name, health):
		self.name 		= name
		self.health 	= health

	def showInfo(self, type):
		print("{} : dengan health : {} : tipe {} ".format(self.name, type, self.health))

class HeroIntelegent(Hero):
	def __init__(self, name):
		Hero.__init__(self, name, 200)
		#super().__init__(name, 200)

	def showInfo(self):
		super().showInfo("intelgent")

class HeroSuper(Hero):
	def __init__(self, name):
		Hero.__init__(self, name, 300)

snipper = HeroIntelegent("jos")
superjitu = HeroSuper("super jitu")

print(snipper.name, " ", snipper.health)
print(superjitu.name, " ", superjitu.health)

snipper.showInfo()
		
		
		