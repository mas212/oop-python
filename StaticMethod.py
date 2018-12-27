class Hero:
	#variabel private
	__jumlah = 0

	def __init__(self, name):
		self.__name = name
		Hero.__jumlah += 1

	#method ini hanya berlaku dengan object
	def getJumlah(self):
		return Hero.__jumlah

	#method ini tidak berlaku untuk object berlaku untuk class
	def getJumlah1():
		return Hero.__jumlah

	#method static nempel di object & object
	@staticmethod 
	def getJumlah2():
		return Hero.__jumlah

	@classmethod
	def getJumlah3(cls):
		return cls.__jumlah

sniper = Hero("mas")
jos = Hero("mama")
print(Hero.getJumlah2())
print(Hero.getJumlah3())
print(sniper.getJumlah2())
