"""Made by Michael Chung"""
import pygame
import random

#https://www.youtube.com/watch?v=kPxokkQlcFc

class MusicPlayer(object):
	def __init__(self):
		self.musictracks = ["storm.ogg", "onetruth.ogg", "suprise.ogg", "fire.ogg"]
		self.mapmusic = ["woods.ogg"]
		self.innmusic = ["joy.ogg"]
		self.townmusic = ["town.ogg"]
		self.barmusic = "mask.ogg"
		self.toughmusic = ["tough.ogg", "rejected.ogg"]
		self.bossmusic = "wave.ogg"
		self.titlescreen = "thread.ogg"
		pygame.mixer.music.set_volume(50)

	def battleStart(self):
		pygame.mixer.music.load(self.musictracks[random.randint(0, len(self.musictracks) - 1)])
		pygame.mixer.music.play(-1)

	def toughbattleStart(self):
		pygame.mixer.music.load(self.toughmusic[random.randint(0, len(self.toughmusic) - 1)])
		pygame.mixer.music.play(-1)

	def Stop2(self):
		pygame.mixer.music.stop()

	def Stop(self):
		pygame.mixer.music.fadeout(3000)


	def Stop3(self):
		pygame.mixer.music.fadeout(1500)

	def title(self):
		pygame.mixer.music.load(self.titlescreen)
		pygame.mixer.music.play(-1)

	def Rewind(self):
		pygame.mixer.music.rewind()

	def mazeStart(self):
		pygame.mixer.music.load(self.mapmusic[random.randint(0, len(self.mapmusic) - 1)])
		pygame.mixer.music.play(-1)

	def townStart(self):
		pygame.mixer.music.load(self.townmusic[random.randint(0, len(self.townmusic) - 1)])
		pygame.mixer.music.play(-1)

	def townStart(self):
		pygame.mixer.music.load(self.townmusic[random.randint(0, len(self.townmusic) - 1)])
		pygame.mixer.music.play(-1)

	def startInn(self):
		pygame.mixer.music.load(self.innmusic[0])
		pygame.mixer.music.play(-1)

	def startBar(self):
		pygame.mixer.music.load(self.barmusic)
		pygame.mixer.music.play(-1)

	def bossStart(self):
		pygame.mixer.music.load(self.bossmusic)
		pygame.mixer.music.play(-1)