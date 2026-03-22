import pygame

pygame.init()
pygame.joystick.init()

# Detect controllers
joystick_count = pygame.joystick.get_count()
print(f"Controllers found: {joystick_count}")

if joystick_count > 0:
    controller = pygame.joystick.Joystick(0)
    controller.init()
    print(f"Using controller: {controller.get_name()}")

for event in pygame.event.get():
    if event.type == pygame.JOYBUTTONDOWN:
        print(f"Button {event.button} pressed")

    if event.type == pygame.JOYAXISMOTION:
        print(f"Axis {event.axis} moved to {event.value}")

    if event.type == pygame.JOYHATMOTION:
        print(f"Hat {event.hat} moved to {event.value}")