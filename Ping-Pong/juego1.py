import pygame, sys
from pygame.locals import *

#Tamaño
size = (600, 450)
### Clases -------------------------------------------------------------
class Bola(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = Cargar_img("img/ball.png", True)
		self.rect = self.image.get_rect()
		self.rect.x = (size[0])/2
		self.rect.y = (size[1])/2
		self.speed = [0.5, -0.5]
	
	def actualizar(self, time, pala_jug, pala_cpu):
		self.rect.x += self.speed[0] * time
		self.rect.y += self.speed[1] * time
		if self.rect.left <= 0 or self.rect.right >= size[0]:
			self.speed[0] = -self.speed[0]
			self.rect.x += self.speed[0] *time

		if self.rect.top <= 0 or self.rect.bottom >= size[1]:
			self.speed[1] = -self.speed[1]
			self.rect.y += self.speed[1] *time

		##Pala del jugador 1
		if pygame.sprite.collide_rect(self, pala_jug):
			self.speed[0] = -self.speed[0]
			self.rect.x += self.speed[0]*time

		##Pala del CPU
		if pygame.sprite.collide_rect(self, pala_cpu):
			self.speed[0] = -self.speed[0]
			self.rect.x += self.speed[0]*time

class Pala (pygame.sprite.Sprite):
	def __init__ (self, x):
		pygame.sprite.Sprite.__init__(self)
		self.image = Cargar_img("img/pala.png")
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = size[1]/2
		self.speed = 0.5
	
	def mover(self, time, keys):
		if self.rect.top >=0:
			if keys[K_UP]:
				self.rect.y -= self.speed*time
		if self.rect.bottom <= size[0]:
			if keys[K_DOWN]:
				self.rect.y += self.speed *time

	def mov2(self, time, ball):
		if ball.speed[0] >= 0 and ball.rect.x >= size[0]/2:
			if self.rect.y < ball.rect.y:
				self.rect.y += self.speed*time
			if self.rect.y > ball.rect.y:
				self.rect.y -=self.speed*time

## ---------------------------------------------------------------------

def Cargar_img(nombre, transparent= False):
	try:
		image = pygame.image.load(nombre)
	except:
		raise SystemExit
	image = image.convert()
	if transparent:
		color = image.get_at((0, 0))
		image.set_colorkey(color, RLEACCEL)
	return image


def main():
	pantalla = pygame.display.set_mode(size)
	pygame.display.set_caption("Pruebas")
	fondo = Cargar_img("img/fondo_pong.png")
	ball = Bola()
	##Pala del jugador 1
	pala_jug = Pala(30)
	##Pala del CPU
	pala_cpu = Pala(size[0]-30)
	clock = pygame.time.Clock()

	while True:
		time = clock.tick(60)
		keys = pygame.key.get_pressed()
		for eventos in pygame.event.get():
			if eventos.type == QUIT:
				sys.exit(0)

		ball.actualizar(time, pala_jug, pala_cpu)
		pala_jug.mover(time, keys)
		pala_cpu.mov2(time, ball)
		pantalla.blit(fondo, (0,0))
		pantalla.blit(ball.image, ball.rect)
		pantalla.blit(pala_jug.image, pala_jug.rect)
		pantalla.blit(pala_cpu.image, pala_cpu.rect)
		pygame.display.flip()
	return 0

if __name__ == "__main__":
	pygame.init()
	main()