class Hero:

	def __init__(self, name):
		self.healt_pool = [0, 100, 200, 300, 400, 500]
		self.attPower_pool = [0, 10, 20, 30, 40, 50]
		self.ammor_pool = [0, 1, 2, 3, 4, 5]
		self.__name = name
		self.__exp = 0
		self.__level = 0

	def showInfo(self):
		print("{} \n\tlevel: {} \n\thealt: {} \n\tattpower: {} \n\tarmor : {}".format(
			self.__name,
			self.__level,
			self.__healt,
			self.__attPower,
			self.__ammor
		))

	@property
	def healt_pool(self):
		pass

	@property
	def attackpower_pool(self):
		pass

	@property
	def ammor_pool(self):
		pass

	@property
	def levelUp(self):
		pass

	@property
	def getExp(self):
		pass

	@healt_pool.setter
	def healt_pool(self, input):
		self.__healt_pool = input

	@attackpower_pool.setter
	def attackpower_pool(self, input):
		self.__attackpower_pool = input

	@ammor_pool.setter
	def ammor_pool(self, input):
		self.__ammor_pool = self

	@gainExp.setter
	def gainExp(self, input):
		self.__exp += input
		if(self.__exp >= 100):
			self.levelUp = self.__exp//100
			self.__exp %= 100

class HeroIntelegent(Hero):
	def __init__(self, name):
		super().__init__(name)
		self.healt_pool = [0, 200, 300, 400, 500, 600]
		self.attackpower_pool = [0, 20, 30, 40, 60]
		self.ammor_pool = [0, 1, 2, 3, 4, 5]
		self.levelUp = 2

class HeroStrenght(Hero):
	def __init__(self, name):
		super.__init__(name)
		self.healt_pool = [0, 300, 400, 500, 600, 700]
		self.attackpower_pool = [0, 30, 40, 50, 60]
		self.ammor_pool = [0, 1, 2, 3, 4, 5]
		self.levelUp = 3
