class Hero:

	def __init__(self, name, health, attackPower, ammor):
		self.name 			= name
		self.health			= health
		self.attackPower 	= attackPower
		self.ammor 			= ammor

	def serang(self, lawan):
		print(self.name + ' menyerang '+ lawan.name)
		lawan.diserang(self, self.attackPower)
	def diserang(self, lawan, attackPower_lawan):
		print(self.name + ' diserang '+ lawan.name)
		attackPower_terima = attackPower_lawan/self.ammor
		print(" serangan terasa "+ attackPower_terima)
		self.health -= attackPower_terima
snipper = Hero("galan", 100, 70, 20)
mas  	= Hero("latief", 100, 80, 20)

snipper.serang(mas)
mas.serang(snipper)

		