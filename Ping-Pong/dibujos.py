import pygame
pygame.init()

# Colores
NEGRO =  (0,0,0)
AZUL = (26, 46, 242)
BLANCO = (255,255,255)
VERDE = (0,255,0)
ROJO = (255,0,0)

# Constantes
Tam = (400,500)
PI = 3.141592653

pantalla = pygame.display.set_mode(Tam)
#Titulo
pygame.display.set_caption("Titulo nuevo")
hecho = True
##Reloj

while not hecho:
	for evento in pygame.event.get():
		if evento.type == pygame.QUIT:
			hecho = True
	pantalla.fill(BLANCO)
	pygame.draw.line(pantalla, VERDE, [0, 0], [100,100], 5)
	#pygame.display.flip()
