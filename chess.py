import pygame
from figure import figure
from pygame.sprite import spritecollide as sc

print(figure)

pygame.init()

VISINA = 800
SIRINA = 800

ekran = pygame.display.set_mode([SIRINA, VISINA])
ura = pygame.time.Clock()

background = pygame.image.load("sahovnica.png")
ekran.blit(background, (0, 0))

koordinate = []
koordinate_beli = []
koordinate_crni = []

beli = pygame.sprite.Group()
crni = pygame.sprite.Group()
poteza_beli = True

class Figura(pygame.sprite.Sprite):
	def __init__(self, figura = "", poljex = 0, poljey = 0, nasprotnik = crni, nasp = "crni"):
		super().__init__()
		pygame.sprite.DirtySprite.__init__(self)
		self.figura = figura
		self.poljex = poljex
		self.poljey = poljey
		self.nasprotnik = nasprotnik
		self.fig = figura
		self.nasp = nasp

		
		self.izbrana = False

		self.image = pygame.Surface((100, 100), pygame.SRCALPHA)
		self.rect = self.image.get_rect() 
		self.slike = pygame.image.load("spritesheetchess1.png")


		if self.figura == "kmetb":
			self.image.blit (self.slike, (0,0), (500, 0, 600, 100))

		if self.figura == "kraljb":
			self.image.blit (self.slike, (0,0), (0, 0, 100, 100))

		if self.figura == "kraljicab":
			self.image.blit (self.slike, (0,0), (100, 0, 200, 100))

		if self.figura == "trdnjavab":
			self.image.blit (self.slike, (0,0), (400, 0, 500, 100))

		if self.figura == "laufarb":
			self.image.blit (self.slike, (0,0), (200, 0, 300, 100))

		if self.figura == "konjb":
			self.image.blit (self.slike, (0,0), (300, 0, 400, 100))


		if self.figura == "kmetc":
			self.image.blit (self.slike, (0,0), (500, 100, 600, 200))

		if self.figura == "kraljc":
			self.image.blit (self.slike, (0,0), (0, 100, 100, 200))

		if self.figura == "kraljicac":
			self.image.blit (self.slike, (0,0), (100, 100, 200, 200))

		if self.figura == "trdnjavac":
			self.image.blit (self.slike, (0,0), (400, 100, 500, 200))

		if self.figura == "laufarc":
			self.image.blit (self.slike, (0,0), (200, 100, 300, 200))

		if self.figura == "konjc":
			self.image.blit (self.slike, (0,0), (300, 100, 400, 200))
		self.rect.x = self.poljey*100
		self.rect.y = self.poljex*100


	def koordinate(self):
		self.kox = self.rect.x/100 + 1
		self.koy = self.rect.y/100 + 1
		self.ko = (self.kox, self.koy)
		koordinate.append(self.ko)
		if self.figura[-1] == "b":
			koordinate_beli.append(self.ko)
		if self.figura[-1] == "c":
			koordinate_crni.append(self.ko)


	def klik(self, pos = (0, 0)):
		self.pos = pos
		if self.ko == self.pos:
			self.izbrana = True
		elif self.izbrana == True:
			self.premik(self.pos)
		

	def premik(self, pos):
		global poteza_beli
		if self.izbrana == True:
			
			self.vx = self.pos[0] - self.ko[0]
			self.vy = self.pos[1] - self.ko[1]
			
			self.novpos = (self.ko[0]+self.vx, self.ko[1]+self.vy)
			
			print(self.figura, poteza_beli)
			if self.mozne_poteze(self.novpos) == True:
				if (self.figura[-1] == "b" and poteza_beli == True) or (self.figura[-1] == "c" and poteza_beli == False):

					koordinate.append(self.novpos)
					koordinate.remove(self.ko)

					if self.figura[-1] == "b":
						koordinate_beli.remove(self.ko)
						koordinate_beli.append(self.novpos)
					if self.figura[-1] == "c":
						koordinate_crni.remove(self.ko)
						koordinate_crni.append(self.novpos)

					self.ko = self.novpos
					self.rect.x += self.vx*100
					self.rect.y += self.vy*100
					poteza_beli = not poteza_beli

				
			self.izbrana = False
		
		else:
			self.izbrana = False

	def mozne_poteze(self, koor = (0, 0)):
		self.fig = self.fig.replace("b", "")
		self.fig = self.fig.replace("c", "")

		print(self.fig)


		if self.fig == "kraljia":
			if abs(koor[0] - self.ko[0]) == abs(koor[1] - self.ko[1]) or koor[0] == self.ko[0] or koor[1] == self.ko[1]:

				if abs(koor[0] - self.ko[0]) == abs(koor[1] - self.ko[1]): 
					for i in range(1, abs(int(koor[1] - self.ko[1]))-1):
						if koor[0] - self.ko[0] > 0 and koor[1] - self.ko[1] > 0:
							if ((self.ko[0] + i, self.ko[1] + i)) in koordinate:
								return False
						if koor[0] - self.ko[0] > 0 and koor[1] - self.ko[1] < 0:
							if ((self.ko[0] + i, self.ko[1] - i)) in koordinate:
								return False
						if koor[0] - self.ko[0] < 0 and koor[1] - self.ko[1] > 0:
							if ((self.ko[0] - i, self.ko[1] + i)) in koordinate:
								return False
						if koor[0] - self.ko[0] < 0 and koor[1] - self.ko[1] < 0:
							if ((self.ko[0] - i, self.ko[1] - i)) in koordinate:
								return False

				if koor[0] == self.ko[0]:
					for i in range(1, abs(int(koor[1] - self.ko[1]))-1):
						if koor[1] - self.ko[1] > 0:
							if ((koor[0], self.ko[1] + i)) in koordinate:
								return False
						elif koor[1] - self.ko[1] < 0:
							if ((koor[0], self.ko[1] - i)) in koordinate:
								return False

				if koor[1] == self.ko[1]:
					for i in range(1, abs(int(koor[0] - self.ko[0]))-1):
						if koor[0] - self.ko[0] > 0:
							if ((self.ko[0] + i, self.ko[1])) in koordinate:
								return False
						elif koor[0] - self.ko[0] < 0:
							if ((self.ko[0]-i, self.ko[1])) in koordinate:
								return False
				return True

		if self.fig == "kralj":
			if abs(koor[1] - self.ko[1]) > 1 or abs(koor[0] - self.ko[0]) > 1:
				return False

			return True

		if self.fig == "laufar":
			if abs(koor[0] - self.ko[0]) == abs(koor[1] - self.ko[1]): 
				for i in range(1, abs(int(koor[1] - self.ko[1]))-1):
					if koor[0] - self.ko[0] > 0 and koor[1] - self.ko[1] > 0:
						if ((self.ko[0] + i, self.ko[1] + i)) in koordinate:
							return False
					if koor[0] - self.ko[0] > 0 and koor[1] - self.ko[1] < 0:
						if ((self.ko[0] + i, self.ko[1] - i)) in koordinate:
							return False
					if koor[0] - self.ko[0] < 0 and koor[1] - self.ko[1] > 0:
						if ((self.ko[0] - i, self.ko[1] + i)) in koordinate:
							return False
					if koor[0] - self.ko[0] < 0 and koor[1] - self.ko[1] < 0:
						if ((self.ko[0] - i, self.ko[1] - i)) in koordinate:
							return False
				return True

		if self.fig == "trdnjava":
			if koor[0] == self.ko[0]:
				for i in range(1, abs(int(koor[1] - self.ko[1]))-1):
					if koor[1] - self.ko[1] > 0:
						if ((koor[0], self.ko[1] + i)) in koordinate:
							print((koor[0], self.ko[1] + i))
							return False
					elif koor[1] - self.ko[1] < 0:
						if ((koor[0], self.ko[1] - i)) in koordinate:
							print((koor[0], self.ko[1] - i))
							return False
				return True

			if koor[1] == self.ko[1]:
				for i in range(1, abs(int(koor[0] - self.ko[0]))-1):
					if koor[0] - self.ko[0] > 0:
						if ((self.ko[0] + i, self.ko[1])) in koordinate:
							return False
					elif koor[0] - self.ko[0] < 0:
						if ((self.ko[0]-i, self.ko[1])) in koordinate:
							return False
				return True


		if self.fig == "konj":
			if abs(koor[0] - self.ko[0]) == 2 and abs(koor[1] - self.ko[1]) == 1:
				return True
			return abs(koor[0] - self.ko[0]) == 1 and abs(koor[1] - self.ko[1]) == 2

		if self.fig == "kmet":
			if self.figura == "kmetb":
				if self.ko[0] == 2 and ((self.ko[0]+1, koor[1])) not in koordinate and ((self.ko[0]+2, koor[1])) not in koordinate and self.ko[0] - koor[0] == -2:
					if self.ko[1] == koor[1]:	
						return True
				elif ((koor[0], koor[1])) not in koordinate and self.ko[0] - koor[0] == -1:
					if self.ko[1] == koor[1]:	
						return True
			if self.figura == "kmetc":
				if self.ko[0] == 7 and ((self.ko[0]-1, koor[1])) not in koordinate and ((self.ko[0]-2, koor[1])) not in koordinate and self.ko[0] - koor[0] == 2:
					if self.ko[1] == koor[1]:	
						return True
				elif ((koor[0]-1, koor[1])) not in koordinate and self.ko[0] - koor[0] == 1:
					if self.ko[1] == koor[1]:	
						return True
		
	def update(self):
		if self.figura[-1] == "b" and poteza_beli == False:
			if self.ko in koordinate_crni:
				sc(self, self.nasprotnik, True)
		if self.figura[-1] == "c" and poteza_beli == True:
			if self.ko in koordinate_beli:
				sc(self, self.nasprotnik, True)



beli.add(Figura("kraljb", 4, 0))
beli.add(Figura("kraljicab", 3, 0))
beli.add(Figura("trdnjavab", 0, 0))
beli.add(Figura("trdnjavab", 7, 0))
beli.add(Figura("laufarb", 2, 0))
beli.add(Figura("laufarb", 5, 0))
beli.add(Figura("konjb", 1, 0))
beli.add(Figura("konjb", 6, 0))
for i in range(8):
	beli.add(Figura("kmetb", i, 1))

crni.add(Figura("kraljc", 4, 7, beli, "beli"))
crni.add(Figura("kraljicac", 3, 7, beli, "beli"))
crni.add(Figura("trdnjavac", 0, 7, beli, "beli"))
crni.add(Figura("trdnjavac", 7, 7, beli, "beli"))
crni.add(Figura("laufarc", 2, 7, beli, "beli"))
crni.add(Figura("laufarc", 5, 7, beli, "beli"))
crni.add(Figura("konjc", 1, 7, beli, "beli"))
crni.add(Figura("konjc", 6, 7, beli, "beli"))
for i in range(8):
	crni.add(Figura("kmetc", i, 6))

for Figura in beli:
	Figura.koordinate()
for FIgura in crni:
	FIgura.koordinate()


igramo = True
while igramo:
	ura.tick(60)
	for dogodek in pygame.event.get():
		if dogodek.type == pygame.QUIT:
			igramo = False
		if dogodek.type == pygame.MOUSEBUTTONUP:
			x, y = dogodek.pos
			x = x//100 +1
			y = y//100 +1
			pos = (x, y)
			for Figura in beli:
				Figura.klik(pos)
			for Figura in crni:
				Figura.klik(pos)

	ekran.blit(background, (0, 0))		
	beli.update()
	beli.draw(ekran)
	crni.update()
	crni.draw(ekran)
	pygame.display.flip()

pygame.quit()