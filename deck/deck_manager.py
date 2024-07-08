from decorator import *
import random

@singleton
class DeckManager:
	
	def __init__(self) -> None:
		self.deck = []			# 牌堆
		self.draw_pile = []		# 抽牌堆
		self.discard_pile = []	# 弃牌堆
		self.consume_pile = []	# 消耗牌堆
		self.hand = []			# 手牌
		self.size = 0

	# 单次抽牌
	def drawCard(self):
		if len(self.draw_pile) == 0:
			self.shuffle()
			if len(self.draw_pile) == 0:
				print("抽牌堆中没有牌可抽了！")
				return
		card = self.draw_pile[0]
		self.hand.append(card)
		del self.draw_pile[0]

	def addCard(self, card):
		self.deck.append(card)
		self.size += 1

	def addCards(self, cards):
		for card in cards:
			self.deck.append(card)
			self.size += 1

	# 洗牌
	def shuffle(self):
		for card in self.discard_pile:
			self.draw_pile.append(card)
		self.discard_pile = []
		random.shuffle(self.draw_pile)