class Hero: #template

	#class variabel
	jumlah = 0
	
	def __init__(self, inputName, inputHealth, inputAttack, InputAmor):
		#instance
		self.name 		= inputName
		self.health 	= inputHealth
		self.attack 	= inputAttack
		self.amor 		= InputAmor
		Hero.jumlah += 1
	
	#method tanpa return
	def siapa(self):
		print("ini dengan siapa" + self.name)

	#method argument
	def health(self, up):
		self.health += up

	#method return
	def getHealth(self):
		return self.health 

hero1 = Hero("sniper", 90, 99, "yes")
print(Hero.jumlah)
hero2 = Hero("bowo", 80, 99, "oke")
print(Hero.jumlah)

hero1.siapa()

print(hero2.healt(100))
hero1.getHealth()

