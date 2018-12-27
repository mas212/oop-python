class Hero:
	def __init__(self, name, healt, armor):
		self.__name = name
		self.__healt = healt
		self.__armor = armor
		self.__info = " name {}: \nhealt {}:".format(self.__name, self.__healt)

	@property
	def info(self):
		return self.__info

	@property
	def armor(self):
		pass

	@armor.getter
	def armor(self):
		return self.__armor

	@armor.setter
	def armor(self):
		return self.__armor

	@armor.deleter
	def armor(self):
		return self.__armor 

snipper = Hero("mas", 100, 5)
print(snipper.info)
print(snipper.__dict__)
print("getter & setter")
print(snipper.armor)
print("setter")
snipper.armor = 100
print(snipper.armor)
print(snipper.__dict__)
del snipper.armor