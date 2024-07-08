from abc import ABC, abstractmethod

class BaseHero(ABC):

	@abstractmethod
	def __init__(self):
		self.id = 1000
		self.name = ""
		self.max_health = 0
		self.health = self.max_health
		self.gold = 0
		self.equips = {}

	def ShowMessage(self):
		print(self.name)
		print("血量", self.max_health)
		print("金币", self.gold)