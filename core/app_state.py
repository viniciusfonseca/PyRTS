import pygame

screen_width, screen_height = 320, 200
scaling_factor = 3

class AppState():
    screen = pygame.Surface((screen_width, screen_height))
    window = pygame.display.set_mode((
        screen_width * scaling_factor,
        screen_height * scaling_factor
    ))
    select_origin = (None, None)
    selecting = False
    running = True
    screen_width = screen_width
    screen_height = screen_height
    scaling_factor = scaling_factor

app_state = AppState()