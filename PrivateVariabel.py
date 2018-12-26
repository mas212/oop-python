class Hero:

	#class variabel
	jumlah = 0
	__privateJumlah = 0

	def __init__(self, name , health):
		self.name 		= name
		self.health 	= health

		#variabel instance private
		self.__private = "private"

		#variabel protected  
		self._protected = "protected"

list = Hero("x-team", 2000)

print(list.__dict__)