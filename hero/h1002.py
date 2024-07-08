from hero.core import BaseHero

class Hero(BaseHero):
	
	def __init__(self):
		self.id = 1002
		self.name = "孙坚"
		self.max_health = 70
		self.health = self.max_health
		self.gold = 99
		self.equips = {}
