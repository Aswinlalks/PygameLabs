import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1200, 600))
pygame.display.set_caption("Background Example")

# Load the background image
background_image = pygame.image.load("01.png")
background_image = pygame.transform.scale(background_image, (1200, 600))

# Load the dcmotor image
dcmotor = pygame.image.load("dcmotor.png")
shelf = pygame.image.load("shelf.png")
shelf = pygame.transform.scale(shelf, (400, 500))

# Get the original width and height of the dcmotor image
original_width, original_height = dcmotor.get_size()

# Define the initial desired width
desired_width = 90

# Calculate the proportional height based on the initial desired width
proportional_height = int(original_height * (desired_width / original_width))

# Scale the dcmotor image proportionally
dcmotor = pygame.transform.scale(dcmotor, (desired_width, proportional_height))

# Define the initial position of the dcmotor image
motor_x = 40
motor_y = 150

# Define the initial position of the shelf image
shelf_x = -50
shelf_y = 100

# Define the zoom factor
zoom_factor = 1.0

# Variable to track if the dcmotor image is being dragged
dragging_motor = False

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button clicked
                # Check if the mouse click is within the bounds of the dcmotor image
                mouse_x, mouse_y = event.pos
                if motor_x <= mouse_x <= motor_x + desired_width * zoom_factor and motor_y <= mouse_y <= motor_y + proportional_height * zoom_factor:
                    dragging_motor = True
                    # Calculate the offset between the mouse click position and the top-left corner of the dcmotor image
                    offset_x = mouse_x - motor_x
                    offset_y = mouse_y - motor_y
            elif event.button == 4:  # Scroll up
                # Increase the zoom factor
                zoom_factor += 0.01
            elif event.button == 5:  # Scroll down
                # Decrease the zoom factor, but ensure it doesn't go below 0.1
                zoom_factor = max(0.1, zoom_factor - 0.1)
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button released
                dragging_motor = False
        elif event.type == pygame.MOUSEMOTION:
            # If the dcmotor image is being dragged, update its position based on the mouse movement
            if dragging_motor:
                # Adjust mouse position based on the zoom factor
                adjusted_mouse_x, adjusted_mouse_y = event.pos
                adjusted_mouse_x /= zoom_factor
                adjusted_mouse_y /= zoom_factor
                motor_x, motor_y = adjusted_mouse_x - offset_x, adjusted_mouse_y - offset_y

    screen.fill((0, 0, 0))  # Fill the screen with black color

    # Draw the background image on the screen
    screen.blit(background_image, (0, 0))

    # Draw the shelf image on the screen at its current position
    screen.blit(shelf, (shelf_x, shelf_y))

    # Calculate the scaled width and height of the dcmotor image based on the zoom factor
    scaled_width = int(desired_width * zoom_factor)
    scaled_height = int(proportional_height * zoom_factor)

    # Scale the dcmotor image based on the zoom factor
    scaled_dcmotor = pygame.transform.scale(dcmotor, (scaled_width, scaled_height))

    # Draw the scaled dcmotor image on the screen at its current position
    screen.blit(scaled_dcmotor, (motor_x, motor_y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
