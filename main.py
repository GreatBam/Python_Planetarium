# Planetarium

# Imports
import pygame
from sun import Sun
from planet import Planet
from orbit import Orbit

# Constants
WIDTH = 800
HEIGHT = 800

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (150, 150, 150)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

# Pygame setup
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planetarium")
running = True

# Planets
sun = Sun(400, 400, 40, YELLOW, screen)
venus = Planet (400, 400, 50, 100, 10, GREY, screen, 0.01, WIDTH, HEIGHT)
mercury = Planet (400, 400, 100, 150, 15, ORANGE, screen, 0.005, WIDTH, HEIGHT)
earth = Planet (400, 400, 150, 200, 20, BLUE, screen, 0.003, WIDTH, HEIGHT)
mars = Planet (400, 400, 200, 250, 25, RED, screen, 0.002, WIDTH, HEIGHT)

# Orbits
venus_orbit = Orbit(200, 100, WHITE, screen)
mercury_orbit = Orbit(300, 200, WHITE, screen)
earth_orbit = Orbit(400, 300, WHITE, screen)
mars_orbit = Orbit(500, 400, WHITE, screen)

# Main loop
while running:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # Logic
    screen.fill(BLACK)
    sun.draw()
    venus_orbit.draw()
    mercury_orbit.draw()
    earth_orbit.draw()
    mars_orbit.draw()
    venus.move()
    mercury.move()
    earth.move()
    mars.move()
    
    # Draw
    pygame.display.flip()
    clock.tick(60)
    
# Close window on quit
pygame.quit()