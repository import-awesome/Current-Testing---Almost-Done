"""Made by Michael Chung"""

import pygame
import math
import items

pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
GREY = (30, 30, 30)
RED = (255, 0, 0)
GOLD = (255, 255, 0)
clock = pygame.time.Clock()

class Character(object):
	def __init__(self, base, level, name, abilities = []):
		self.name = name #raw_input("Enter Character Name: ")
		self.level = level
		self.hp = base[0]
		self.mhp = base[1]
		self.mp = base[2]
		self.mmp = base[3]
		self.stats = base[4]
		self.exp = 0
		self.nexp = 100
		self.equip = base[5]
		self.physattk = base[6]
		self.physdefence = base[7]
		self.defend = 0
		self.food = 0
		self.drink = 0
		self.abilities = []
		self.boss = 0

	def isDead(self):
		if self.hp <= 0:
			self.hp = 0
			return True

		return False

	def lvlup(self, gain):
		if gain + self.exp >= self.nexp:
			temp = self.exp + gain - self.nexp
			self.stats[1] += 5
			self.stats[0] += 5
			self.nexp = self.nexp + (self.level * self.nexp)
			self.exp = temp
			return True

		return False

class Land(Character):
	def __init__(self):
		base = [48, 48, 26, 26, [9, 5, 8, 6, 4], ["", "", "", ""], 24, 17]
		self.abilities = ["Pummel", 10, 5]
		Character.__init__(self, base, 1, "Demi")


class Night(Character):
	def __init__(self):
		base = [37, 37, 29, 29, [8, 7, 4, 10, 8], ["", "", "", ""], 24, 12]
		self.abilities = ["Silent Strike", 8, 5]
		Character.__init__(self, base, 1, "Jyokaa")


class Fort(Character):
	def __init__(self):
		base = [52, 52, 21, 21, [5, 6, 11, 13, 6], ["", "", "", ""], 22, 20]
		self.abilities = ["Blade Fury", 10, 5]
		Character.__init__(self, base, 1, "Wings")


class Medic(Character):
	def __init__(self):
		base = [40, 40, 39, 39, [5, 10, 6, 6, 5], ["", "", "", ""], 22, 14]
		self.abilities = ["Heal Party", 0, 8]
		Character.__init__(self, base, 1, "Mint")


class Rune(Character):
	def __init__(self):
		base = [31, 31, 42, 42, [4, 11, 4, 5, 6], ["", "", "", ""], 22, 12]
		self.abilities = ["Fire Bow", 9, 6]
		Character.__init__(self, base, 1, "Oracle")

class Boss(Character):
	def __init__(self):
		base = [1200, 1200, 400, 400, [15, 7, 7, 8, 6], ["", "", "", ""], 200, 15]
		Character.__init__(self, base, 10, "Medusa")
		self.boss = 1

class babyDragon(Character):
	def __init__(self):
		base = [16, 16, 24, 24, [3, 3, 3, 3, 3], ["", "", "", ""], 12, 12]
		self.xp = 5
		self.image = "babydrag.png"
		Character.__init__(self, base, 1, "Drag", [])

class elderDragon(Character):
	def __init__(self):
		base = [22, 22, 30, 30, [6, 6, 6, 6, 6], ["", "", "", ""], 18, 18]
		self.xp = 10
		self.image = "elderdrag.png"
		Character.__init__(self, base, 1, "Behemoth", [])

class bug(Character):
	def __init__(self):
		base = [18, 18, 27, 27, [5, 5, 5, 5, 5], ["", "", "", ""], 15, 15]
		self.xp = 8
		self.image = "bug.png"
		Character.__init__(self, base, 1, "Ochu", [])

class grapeApe(Character):
	def __init__(self):
		base = [20, 20, 26, 26, [6, 6, 6, 6, 6], ["", "", "", ""], 18, 18]
		self.xp = 9
		self.image = "grapeape.png"
		Character.__init__(self, base, 1, "Kong", [])

class madElephant(Character):
	def __init__(self):
		base = [17, 17, 24, 24, [4, 4, 4, 4, 4], ["", "", "", ""], 14, 14]
		self.xp = 7
		self.image = "madelephant.png"
		Character.__init__(self, base, 1, "Jumbo", [])

class mantis(Character):
	def __init__(self):
		base = [16, 16, 24, 24, [3, 3, 3, 3, 3], ["", "", "", ""], 12, 12]
		self.xp = 6
		self.image = "mantis.png"
		Character.__init__(self, base, 1, "Scyther", [])

class phoenix(Character):
	def __init__(self):
		base = [19, 19, 25, 25, [4, 4, 4, 4, 4], ["", "", "", ""], 13, 13]
		self.xp = 8
		self.image = "phoenix.png"
		Character.__init__(self, base, 1, "Chimera", [])

if __name__ == "__main__":
	c = Rune()
	print c.name
