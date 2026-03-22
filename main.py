import pygame
from platforms import load_platforms

pygame.init()

# Window setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Circle + Square Demo")

clock = pygame.time.Clock()
running = True

# Camera
camera_x = 0
camera_y = 0
deadzone_width = 200
deadzone_height = 150

# Realistic stuff
gravity = 0.5

# Player (circle visual, rect hitbox)
player_x = 200
player_y = 200
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 50
player_radius = 25
player_speed = 5
player_vel_y = 0
on_ground = False

# Squares
static_square = pygame.Rect(700, 400, 100, 100)

movable_square = pygame.Rect(400, 150, 100, 100)
square_speed = 4
square_vel_y = 0

# Platforms
platforms = load_platforms()  # list of pygame.Rect

def get_player_rect():
    return pygame.Rect(
        int(player_x - PLAYER_WIDTH // 2),
        int(player_y - PLAYER_HEIGHT // 2),
        PLAYER_WIDTH,
        PLAYER_HEIGHT
    )

def draw_grid(surface, camera_x, camera_y, grid_size=50):
    color = (60, 60, 60)
    start_x = int(-camera_x % grid_size)
    start_y = int(-camera_y % grid_size)

    for x in range(start_x, WIDTH, grid_size):
        pygame.draw.line(surface, color, (x, 0), (x, HEIGHT))

    for y in range(start_y, HEIGHT, grid_size):
        pygame.draw.line(surface, color, (0, y), (WIDTH, y))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()


    # Horizontal input
    square_dx = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * square_speed

    # Apply horizontal movement
    movable_square.x += square_dx

    # Horizontal collision (only horizontal)
    for rect in platforms + [static_square]:
        if movable_square.colliderect(rect):
            if square_dx > 0:
                movable_square.right = rect.left
            elif square_dx < 0:
                movable_square.left = rect.right

    # Gravity
    square_vel_y += gravity
    movable_square.y += square_vel_y

    # Vertical collision (only vertical)
    for rect in platforms + [static_square]:
        if movable_square.colliderect(rect):
            if square_vel_y > 0:
                movable_square.bottom = rect.top
                square_vel_y = 0
            elif square_vel_y < 0:
                movable_square.top = rect.bottom
                square_vel_y = 0
    
    # Horizontal stuff
    dx = (keys[pygame.K_d] - keys[pygame.K_a])

    player_rect = get_player_rect()
    player_rect.x += dx * player_speed

    solids = platforms + [static_square, movable_square]

    for rect in solids:
        if player_rect.colliderect(rect):
            if dx > 0:  # moving right
                player_rect.right = rect.left
            elif dx < 0:  # moving left
                player_rect.left = rect.right

    player_x = player_rect.centerx

    # circle movment
    player_vel_y += gravity
    player_rect.y += player_vel_y
    on_ground = False

    for rect in solids:
        if player_rect.colliderect(rect):
            if player_vel_y > 0:  # falling
                player_rect.bottom = rect.top
                player_vel_y = 0
                on_ground = True
            elif player_vel_y < 0:  # jumping up
                player_rect.top = rect.bottom
                player_vel_y = 0

    player_y = player_rect.centery

    # Jump
    if on_ground and keys[pygame.K_SPACE]:
        player_vel_y = -12
        on_ground = False

    # Camera things
    left_bound = camera_x + (WIDTH - deadzone_width) // 2
    right_bound = camera_x + (WIDTH + deadzone_width) // 2
    top_bound = camera_y + (HEIGHT - deadzone_height) // 2
    bottom_bound = camera_y + (HEIGHT + deadzone_height) // 2

    if player_x < left_bound:
        camera_x = player_x - deadzone_width // 2
    elif player_x > right_bound:
        camera_x = player_x - (WIDTH - deadzone_width // 2)

    if player_y < top_bound:
        camera_y = player_y - deadzone_height // 2
    elif player_y > bottom_bound:
        camera_y = player_y - (HEIGHT - deadzone_height // 2)

    # making the world
    screen.fill((30, 30, 30))
    draw_grid(screen, camera_x, camera_y)

    # Player (circle, centered on rect)
    pygame.draw.circle(
        screen,
        (0, 200, 255),
        (int(player_x - camera_x), int(player_y - camera_y)),
        player_radius
    )

    # Static square
    pygame.draw.rect(
        screen,
        (255, 80, 80),
        pygame.Rect(
            static_square.x - camera_x,
            static_square.y - camera_y,
            static_square.width,
            static_square.height
        )
    )

    # Movable square
    pygame.draw.rect(
        screen,
        (255, 200, 0),
        pygame.Rect(
            movable_square.x - camera_x,
            movable_square.y - camera_y,
            movable_square.width,
            movable_square.height
        )
    )

    # Platforms
    for plat in platforms:
        pygame.draw.rect(
            screen,
            (80, 255, 80),
            pygame.Rect(
                plat.x - camera_x,
                plat.y - camera_y,
                plat.width,
                plat.height
            )
        )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()