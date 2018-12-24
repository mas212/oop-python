class Hero: #template
	
	def __init__(self, inputName, inputHealth, inputAttack, InputAmor):
		#instance
		self.name 		= inputName
		self.health 	= inputHealth
		self.attack 	= inputAttack
		self.amor 		= InputAmor


hero1 = Hero("jos", 90, 99, "yes")
hero2 = Hero("jos1", 80, 99, "oke")

print(hero1.__dict__)
print(hero2.__dict__)