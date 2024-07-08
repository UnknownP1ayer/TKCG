from decorator import *
from hero.core import showHeroMessage
import os

running = True

@singleton
class Menu:

	menu = {
		1: "开始游戏",
		2: "继续游戏",
		3: "游戏介绍",
		4: "退出游戏"
	}

	def ShowMenu(self):
		for idx in self.menu:
			print(idx,".", self.menu[idx])

	def chooseMenu(self):
		print("请输入指令：", end = '')
		command = input()
		if command == '1':
			self.start()
		elif command == '2':
			self.load()
		elif command == '3':
			self.introduce()
		elif command == '4':
			self.end()
		else:
			self.error()

	def start(self):
		os.system('cls')
		showHeroMessage()

	def load(self):
		os.system('cls')

	def introduce(self):
		os.system('cls')

	def end(self):
		global running
		running = False
	
	def error(self):
		print("指令错误，请重新输入")