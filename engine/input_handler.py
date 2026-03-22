class InputHandler:
    def __init__(self, controller=None):
        self.controller = controller

    def get_move_direction(self):
        # Keyboard fallback
        keys = pygame.key.get_pressed()
        x = keys[pygame.K_d] - keys[pygame.K_a]
        y = keys[pygame.K_s] - keys[pygame.K_w]

        # Controller override
        if self.controller:
            x = self.controller.get_axis(0)
            y = self.controller.get_axis(1)

        return x, y