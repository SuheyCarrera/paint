import pygame
import math

class Figura:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def mover(self, dx, dy):
        self.x += dx
        self.y += dy

    def cambiar_color(self, new_color):
        self.color = new_color

    def dibujar(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), 50)
        pygame.display.flip()

class Rectangulo:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def mover(self, dx, dy):
        self.x += dx
        self.y += dy

    def cambiar_color(self, new_color):
        self.color = new_color

    def dibujar(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))
        pygame.display.flip()

# Inicializar Pygame
pygame.init()

# Crear una superficie de 800x600 píxeles, no debe cambiar esta superficie
width = 800 
height = 600
surface = pygame.display.set_mode((width, height))
background_color = (255, 23, 100)
surface.fill(background_color)

# Establecer el color de un píxel en la posición (100, 200) a rojo (255, 0, 0)
color = (255, 120, 10)

# Crear objetos de las clases Figura y Rectangulo
figura1 = Figura(200, 200, (0, 255, 0))
rectangulo1 = Rectangulo(400, 300, 100, 150, (0, 0, 255))

# Definir funciones adicionales necesarias
def linea_h():
    for i in range(0, 100):
        surface.set_at((100 + i, 200), color)
    pygame.display.flip()

def linea_v():
    for i in range(0, 100):
        surface.set_at((100, 200 + i), color)
    pygame.display.flip()

def borrar_ultimo_trazo():
    pygame.draw.rect(surface, background_color, (100, 200, 100, 100))
    pygame.display.flip()

def cambiar_color_fondo(new_color):
    global background_color
    if new_color in color_list:
        background_color = color_list[new_color]
        surface.fill(background_color)
        pygame.display.flip()

def cambiar_color_trazo(new_color):
    global color
    if new_color in color_list:
        color = color_list[new_color]

def ajustar_grosor(new_size):
    global pixel_size
    pixel_size = max(1, new_size)

def dibujar_cuadrado(x, y, size):
    pygame.draw.rect(surface, color, (x, y, size, size))
    pygame.display.flip()

def dibujar_rectangulo(x, y, width, height):
    pygame.draw.rect(surface, color, (x, y, width, height))
    pygame.display.flip()

def dibujar_circulo(x, y, radius):
    pygame.draw.circle(surface, color, (x, y), radius)
    pygame.display.flip()

def dibujar_triangulo_equilatero(x, y, side_length):
    height = side_length * math.sqrt(3) / 2
    pygame.draw.polygon(surface, color, [
        (x, y),
        (x + side_length, y),
        (x + side_length / 2, y - height)
    ])
    pygame.display.flip()

def dibujar_triangulo_escaleno(x, y, side1, side2, side3):
    pygame.draw.polygon(surface, color, [
        (x, y),
        (x + side1, y),
        (x + side3, y - side2)
    ])
    pygame.display.flip()

def dibujar_triangulo_isosceles(x, y, base, height):
    pygame.draw.polygon(surface, color, [
        (x, y),
        (x + base, y),
        (x + base / 2, y - height)
    ])
    pygame.display.flip()

# Lista de colores y sus comandos correspondientes
color_list = {
    "rojo": (255, 0, 0),
    "verde": (0, 255, 0),
    "azul": (0, 0, 255),
    "amarillo": (255, 255, 0),
    "rosa": (255, 0, 255)
}

# Asociar los comandos con las funciones correspondientes
command_list = {
    "linea -h": linea_h,
    "linea -v": linea_v,
    "borrar": borrar_ultimo_trazo,
    "fondo": cambiar_color_fondo,
    "trazo": cambiar_color_trazo,
    "pixelsize": ajustar_grosor,
    "cuadrado": dibujar_cuadrado,
    "rectangulo": dibujar_rectangulo,
    "circulo": dibujar_circulo,
    "triangulo_equilatero": dibujar_triangulo_equilatero,
    "triangulo_escaleno": dibujar_triangulo_escaleno,
    "triangulo_isosceles": dibujar_triangulo_isosceles,
    "figura_mover": figura1.mover,
    "figura_cambiar_color": figura1.cambiar_color,
    "figura_dibujar": figura1.dibujar,
    "rectangulo_mover": rectangulo1.mover,
    "rectangulo_cambiar_color": rectangulo1.cambiar_color,
    "rectangulo_dibujar": rectangulo1.dibujar
}

# Esperar a que el usuario cierre la ventana
running = True
while running:
    cmd = input("cmd> ")
    tokens = cmd.split()
    if tokens[0] in command_list:
        if len(tokens) > 1:
            command_list[tokens[0]](*map(int, tokens[1:]))
        else:
            command_list[tokens[0]]()
    elif cmd.startswith("color "):
        color_name = cmd.split(" ")[1]
        if color_name in color_list:
            color = color_list[color_name]

pygame.quit()
