from hero.core import BaseHero

class Hero(BaseHero):
	
	def __init__(self):
		self.id = 1001
		self.name = "曹操"
		self.max_health = 80
		self.health = self.max_health
		self.gold = 99
		self.equips = {}
