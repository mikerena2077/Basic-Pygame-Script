import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Cube")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up cube parameters
cube_size = 100
cube_pos = ((width - cube_size) // 2, (height - cube_size) // 2)

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(WHITE)

    # Draw the cube
    pygame.draw.rect(screen, BLACK, (cube_pos[0], cube_pos[1], cube_size, cube_size))

    # Update the display
    pygame.display.flip()
