import pygame

def load_platforms():
    return [
        pygame.Rect(300, 400, 300, 40),
        pygame.Rect(100, 300, 200, 40),
        pygame.Rect(10, 500, 500, 40),
        pygame.Rect(0, 0, 50, 4000),
        pygame.Rect(0, 0, 4000, 50),
        pygame.Rect(0, 4000, 4000, 50),
        pygame.Rect(4000, 0, 50, 4000),
        pygame.Rect(900, 350, 300, 40),
        pygame.Rect(1200, 450, 200, 40)
    ]

# Platform (rectangle)
# Horizontal, Verticle, Screen
#platform = pygame.Rect(hs, vs, h, v)