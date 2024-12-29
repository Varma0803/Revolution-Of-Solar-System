import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GREY = (169, 169, 169)
ORANGE = (255, 165, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BROWN = (165, 42, 42)
LIGHT_BLUE = (173, 216, 230)
DARK_BLUE = (0, 0, 139)

# Define planets with their properties
planets = [
    {"name": "Mercury", "color": GREY, "radius": 8, "distance": 70, "speed": 0.02, "angle": 0},
    {"name": "Venus", "color": ORANGE, "radius": 14, "distance": 100, "speed": 0.015, "angle": 0},
    {"name": "Earth", "color": BLUE, "radius": 16, "distance": 140, "speed": 0.01, "angle": 0},
    {"name": "Mars", "color": RED, "radius": 12, "distance": 190, "speed": 0.008, "angle": 0},
    {"name": "Jupiter", "color": BROWN, "radius": 35, "distance": 250, "speed": 0.005, "angle": 0},
    {"name": "Saturn", "color": LIGHT_BLUE, "radius": 30, "distance": 320, "speed": 0.003, "angle": 0},
    {"name": "Uranus", "color": LIGHT_BLUE, "radius": 25, "distance": 400, "speed": 0.002, "angle": 0},
    {"name": "Neptune", "color": DARK_BLUE, "radius": 24, "distance": 470, "speed": 0.0015, "angle": 0},
]

# Sun properties
sun_color = YELLOW
sun_radius = 50
sun_position = (WIDTH // 2, HEIGHT // 2)

# Font for planet names
font = pygame.font.SysFont(None, 24)

# Star properties
num_stars = 100
stars = [(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(num_stars)]

# Comet properties
comet_color = WHITE
comet_radius = 10
comet_position = [0, HEIGHT // 2]
comet_speed = [2, 1]
comet_trail = []

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Draw the stars
    for star in stars:
        screen.set_at(star, WHITE)

    # Draw the Sun
    pygame.draw.circle(screen, sun_color, sun_position, sun_radius)

    # Draw the planets
    for planet in planets:
        x = sun_position[0] + int(planet["distance"] * math.cos(planet["angle"]))
        y = sun_position[1] + int(planet["distance"] * math.sin(planet["angle"]))
        pygame.draw.circle(screen, planet["color"], (x, y), planet["radius"])

        # Draw planet name
        text = font.render(planet["name"], True, WHITE)
        screen.blit(text, (x - text.get_width() // 2, y + planet["radius"] + 5))

        # Update the angle for the planet
        planet["angle"] += planet["speed"]

    # Draw the comet
    pygame.draw.circle(screen, comet_color, comet_position, comet_radius)
    comet_trail.append(tuple(comet_position))

    # Draw the comet's trail
    for i in range(len(comet_trail) - 1):
        pygame.draw.line(screen, comet_color, comet_trail[i], comet_trail[i + 1], 2)

    # Update the comet's position
    comet_position[0] += comet_speed[0]
    comet_position[1] += comet_speed[1]

    # Remove old parts of the trail
    if len(comet_trail) > 50:
        comet_trail.pop(0)

    # Reset comet position if it goes off-screen
    if comet_position[0] > WIDTH or comet_position[1] > HEIGHT or comet_position[0] < 0 or comet_position[1] < 0:
        comet_position = [0, random.randint(0, HEIGHT)]
        comet_trail = []

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
