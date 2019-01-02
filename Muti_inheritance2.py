class Team:

	def setTeam(self, team):
		self.team = team

	def showTeam(self):
		print(self.team)

class Tipe:

	def setTipe(self, tipe):
		self.tipe = tipe

	def showTipe(self):
		print(self.tipe)

class Hero(Team, Tipe):
	
	def __init__(self, name, health):
		self.name = name
		self.health = health

mas = Hero("mas harry", 100)
mas.setTeam("jos")
mas.setTipe("mantap")
mas.showTeam()
mas.showTipe()		