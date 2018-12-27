class Hero:

	def __init__(self, name, health, attackPower):
		self.__name 		= name
		self.__health 		= health
		self.__attpower 	= attackPower

	#getter
	def getName(self):
		return self.__name

	def getHealth(self):
		return self.__health

	#setter
	def setDiserang(self, value):
		self.__health -= value

intanceObject = Hero("phonix", 100, 7)
print(intanceObject.__dict__)

print(intanceObject.getName())
print(intanceObject.getHealth())
intanceObject.setDiserang(80)
print(intanceObject.getHealth())