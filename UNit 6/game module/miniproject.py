import sys
sys.path.append('C:\\Python312\\Lib\\site-packages')
import pygame

# Initialize Pygame
pygame.init()

# Set up the display
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("House Drawing")

# Define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BROWN = (139, 69, 19)
YELLOW = (255, 255, 0)
RED = (255,0,0)
ORANGE = (255,128,0)
GREEN = (0, 128, 0)
BLACK = (0, 0, 0)

# Main loop
while True:
    screen.fill(ORANGE)  # Fill the screen with orange color
    
    # Draw the house body
    pygame.draw.rect(screen, BLUE, (350, 200, 200, 150))  # (x, y, width, height)
    
    # Draw the roof (triangle)
    pygame.draw.polygon(screen, BROWN, [(350, 200), (450, 100), (550, 200)])
    
    # Draw the door
    pygame.draw.rect(screen, BROWN, (425, 280, 50, 70))
    
    # Draw the windows
    pygame.draw.circle(screen, YELLOW, (400, 230), 20)  # Window 1
    pygame.draw.circle(screen, YELLOW, (500, 230), 20)  # Window 2

    # Draw the trunk (rectangle)
    pygame.draw.rect(screen, BROWN, (75, 250, 40, 100))  # (x, y, width, height)
    
    # Draw the leaves (triangle)
    pygame.draw.polygon(screen, GREEN, [(000, 250), (100, 100), (200, 250)])
    pygame.draw.polygon(screen, GREEN, [(20, 200), (100, 50), (180, 200)])
    pygame.draw.polygon(screen, GREEN, [(40, 150), (100, 20), (160, 150)])


    #draw the person
    pygame.draw.circle(screen, BLACK, (670, 200), 30)  # Head
    pygame.draw.line(screen, BLACK, (670, 180), (670, 300), 2)  # Body
    pygame.draw.line(screen, BLACK, (670, 245), (630, 275), 2)  # Left arm
    pygame.draw.line(screen, BLACK, (673, 245), (703, 275), 2)  # Right arm
    pygame.draw.line(screen, BLACK, (670, 300), (630, 330), 2)  # Left leg
    pygame.draw.line(screen, BLACK, (673, 300), (703, 330), 2)  # Right leg

    #draw the bushes
    pygame.draw.circle(screen, GREEN, (235, 335), 25)  # bush 1
    pygame.draw.circle(screen, GREEN, (250, 335), 25)  # bush 2
    pygame.draw.circle(screen, GREEN, (265, 335), 25)  # bush 3
    pygame.draw.circle(screen, GREEN, (220, 335), 25)  # bush 4
    pygame.draw.circle(screen, GREEN, (235, 315), 25)  # bush 5
    pygame.draw.circle(screen, GREEN, (250, 315), 25)  # bush 6
    pygame.draw.circle(screen, GREEN, (265, 315), 25)  # bush 7
    pygame.draw.circle(screen, GREEN, (220, 315), 25)  # bush 8

    #draw the sun
    pygame.draw.circle(screen, YELLOW, (800, 0), 70)  # sun


    # Update the display
    pygame.display.flip()
    
    

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()