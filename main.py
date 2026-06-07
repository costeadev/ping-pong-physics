import pygame
from enum import Enum


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


class Ball:
    def __init__(self, position, x_direction, y_direction):
        self.position = position
        self.x_direction = x_direction
        self.y_direction = y_direction


pygame.init()

WINDOW_SIZE = (1280, 720)

screen = pygame.display.set_mode(WINDOW_SIZE)

clock = pygame.time.Clock()

ball = Ball([WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2], Direction.RIGHT, Direction.DOWN)

while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    mouse_pos = pygame.mouse.get_pos()

    screen.fill("white")  # Fill the display with a solid color

    pygame.draw.line(screen, "green", start_pos=[mouse_pos[0], mouse_pos[1] - 50],
                     end_pos=[mouse_pos[0], mouse_pos[1] + 50], width=10)
    pygame.draw.circle(screen, "red", center=ball.position, radius=10)

    # Right wall
    if ball.position[0] + 10 > WINDOW_SIZE[0]:
        ball.x_direction = Direction.LEFT

    # Left wall
    if ball.position[0] - 10 < 0:
        ball.x_direction = Direction.RIGHT

    # Bottom wall
    if ball.position[1] + 10 > WINDOW_SIZE[1]:
        ball.y_direction = Direction.UP

    # Top wall
    if ball.position[1] - 10 < 0:
        ball.y_direction = Direction.DOWN



    if ball.x_direction == Direction.RIGHT:
        ball.position[0] += 10

    if ball.x_direction == Direction.LEFT:
        ball.position[0] -= 10

    if ball.y_direction == Direction.DOWN:
        ball.position[1] += 10

    if ball.y_direction == Direction.UP:
        ball.position[1] -= 10

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)  # wait until next frame (at 60 FPS)
