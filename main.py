import pygame
from enum import Enum


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class Paddle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Ball:
    def __init__(self, radius, position, speed, x_direction, y_direction):
        self.radius = radius
        self.position = position
        self.speed = speed
        self.x_direction = x_direction
        self.y_direction = y_direction

def paddle_hit_ball():
    if ball.position[0] >= mouse_pos[0] - paddle.width // 2 - ball.radius and ball.position[0] <= mouse_pos[0] + ball.radius + paddle.width // 2 and ball.position[1] >= mouse_pos[1] - ball.radius - paddle.height // 2 and ball.position[1] <= mouse_pos[1] + ball.radius + paddle.height // 2:
        return True
    return False

def calculate_direction_change(x_delta, y_delta):
    if x_delta > 0:
        ball.x_direction = Direction.RIGHT
    if x_delta < 0:
        ball.x_direction = Direction.LEFT
    if y_delta > 0:
        ball.y_direction = Direction.DOWN
    if y_delta < 0:
        ball.y_direction = Direction.UP

def calculate_speed_change(x_delta, y_delta):
    speed_change = (abs(x_delta) + abs(y_delta)) * 0.1
    ball.speed += speed_change

def calculate_flick():
    x_delta = mouse_pos[0] - last_mouse_pos[0]
    y_delta = mouse_pos[1] - last_mouse_pos[1]

    calculate_direction_change(x_delta, y_delta)
    calculate_speed_change(x_delta, y_delta)


pygame.init()

WINDOW_SIZE = (1280, 720)
SCREEN_HALF = [WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2]

last_mouse_pos = (0, 0)

screen = pygame.display.set_mode(WINDOW_SIZE)

clock = pygame.time.Clock()

paddle = Paddle(10 , 50)
ball = Ball(10, SCREEN_HALF, 5, None, None)

while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    mouse_pos = pygame.mouse.get_pos() # Current mouse position

    # print(f"Mouse: ({mouse_pos[0]},{mouse_pos[1]})\n")
    # print(f"Ball: ({ball.position[0]},{ball.position[1]})\n")


    screen.fill("white")  # Fill the display with a solid color

    # Paddle render
    pygame.draw.line(screen, "green", start_pos=[mouse_pos[0], mouse_pos[1] - paddle.height // 2],
                     end_pos=[mouse_pos[0], mouse_pos[1] + paddle.height // 2], width=paddle.width)

    # Ball render
    pygame.draw.circle(screen, "red", center=ball.position, radius=ball.radius)

    # Only when the ball was hit, we will calculate the change in direction
    # We got to find the direction of the flick, if the paddle was flicked up and right, the ball will take that same direction
    if paddle_hit_ball():
        calculate_flick()

    last_mouse_pos = mouse_pos


    # === BALL COLLISIONS ===

    # Right wall
    if ball.position[0] + ball.speed > WINDOW_SIZE[0]:
        ball.x_direction = Direction.LEFT

    # Left wall
    if ball.position[0] - ball.speed < 0:
        ball.x_direction = Direction.RIGHT

    # Bottom wall
    if ball.position[1] + ball.speed > WINDOW_SIZE[1]:
        ball.y_direction = Direction.UP

    # Top wall
    if ball.position[1] - ball.speed < 0:
        ball.y_direction = Direction.DOWN


    # === BALL MOVEMENT ===
    if ball.x_direction == Direction.RIGHT:
        ball.position[0] += ball.speed

    if ball.x_direction == Direction.LEFT:
        ball.position[0] -= ball.speed

    if ball.y_direction == Direction.DOWN:
        ball.position[1] += ball.speed

    if ball.y_direction == Direction.UP:
        ball.position[1] -= ball.speed

    if ball.speed > 0:
        ball.speed -= 2 / 60

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)  # wait until next frame (at 60 FPS)

